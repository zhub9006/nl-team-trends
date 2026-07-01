#!/usr/bin/env python3
"""NL Team Trends Visualization Generator."""
import os, pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.rcParams.update({"figure.figsize":(12,7),"figure.dpi":150,"font.size":11})
COLORS=sns.color_palette("husl",15);DATA_DIR,PLOT_DIR="data","plots";os.makedirs(PLOT_DIR,exist_ok=True)
def load_data():
    return(pd.read_csv(f"{DATA_DIR}/{f}")for f in["nl_historical_data_complete.csv","franchise_summary.csv","era_analysis.csv","nl_team_vs_team.csv"])
def chart1(franchise,era):
    fig,ax=plt.subplots(figsize=(12,8));sf=franchise.sort_values("win_pct",ascending=True);y=range(len(sf))
    ax.barh(y,sf["win_pct"]*100,color=COLORS,height=0.7)
    ax.scatter(era["avg_win_pct"]*100,range(len(era)),s=120,marker="D",color="darkred",zorder=5,label="Era Avg")
    ax.set_yticks(y);ax.set_yticklabels(sf["franchise"],fontsize=10)
    ax.set_xlabel("Win %");ax.set_title("NL Franchise All-Time Win% vs Era Averages",fontsize=15);ax.legend();ax.set_xlim(40,62)
    for i,(_,r)in enumerate(sf.iterrows()):ax.text(r["win_pct"]*100+0.3,i,f'{r["win_pct"]:.3f}',va="center",fontsize=8)
    fig.savefig(f"{PLOT_DIR}/chart1_franchise_era.png",dpi=150);plt.close();print("  Done: Chart 1")
def chart2(hist):
    ew=hist.groupby(["era","team"]).agg(w=("wins","sum"),l=("losses","sum")).reset_index();ew["pct"]=ew["w"]/(ew["w"]+ew["l"])
    eo=["Pre-Modern","Dead Ball","Live Ball","Post-War","Expansion","Divisional","Modern"];ew["eo"]=ew["era"].map({e:i for i,e in enumerate(eo)});ew=ew.sort_values(["team","eo"])
    fig,ax=plt.subplots(figsize=(14,8))
    for i,t in enumerate(ew["team"].unique()):
        d=ew[ew["team"]==t]
        if len(d)>1:ax.plot(d["eo"],d["pct"]*100,marker="o",label=t,color=COLORS[i%15],linewidth=2,markersize=6)
    ax.set_xticks(range(7));ax.set_xticklabels(eo,rotation=30,ha="right");ax.set_ylabel("Win %");ax.set_title("NL Win% by Era",fontsize=15)
    ax.legend(loc="lower left",fontsize=7,ncol=2);ax.set_ylim(35,75);fig.savefig(f"{PLOT_DIR}/chart2_rolling_trends.png",dpi=150);plt.close();print("  Done: Chart 2")
def chart3(hist):
    ew=hist.groupby(["era","modern_name"]).agg(w=("wins","sum"),l=("losses","sum")).reset_index();ew["pct"]=ew["w"]/(ew["w"]+ew["l"])
    pivot=ew.pivot_table(index="modern_name",columns="era",values="pct")
    eo=["Pre-Modern","Dead Ball","Live Ball","Post-War","Expansion","Divisional","Modern"];pivot=pivot.reindex(columns=[e for e in eo if e in pivot.columns])
    fig,ax=plt.subplots(figsize=(12,9));sns.heatmap(pivot*100,annot=True,fmt=".1f",cmap="RdYlGn",vmin=40,vmax=72,center=55,linewidths=.5,ax=ax)
    ax.set_title("NL Team Win% by Era Heatmap",fontsize=15);ax.set_ylabel("Franchise");ax.set_xlabel("Era")
    fig.savefig(f"{PLOT_DIR}/chart3_era_heatmap.png",dpi=150);plt.close();print("  Done: Chart 3")
def chart4(franchise):
    fig,ax=plt.subplots(figsize=(12,8));sf=franchise.sort_values("last_championship",ascending=True);ref=2025
    sf["drought"]=sf.apply(lambda r:ref-r["last_championship"] if r["last_championship"]!="—" and pd.notna(r["last_championship"]) else ref-r["first_season"],axis=1).astype(int);sf=sf.sort_values("drought",ascending=True)
    colors=["#d62728"if d>20 else"#ff7f0e"if d>10 else"#2ca02c"for d in sf["drought"]]
    ax.barh(range(len(sf)),sf["drought"],color=colors,height=0.7)
    ax.set_yticks(range(len(sf)));ax.set_yticklabels(sf["franchise"],fontsize=10)
    ax.set_xlabel("Years Since Last WS Title");ax.set_title("NL Championship Drought Tracker (2025)",fontsize=15)
    for i,(_,r)in enumerate(sf.iterrows()):ws=r["ws_titles"]if pd.notna(r["ws_titles"])else 0;ax.text(r["drought"]+0.5,i,f'{r["drought"]}y ({int(ws)} WS)',va="center",fontsize=8)
    ax.set_xlim(0,sf["drought"].max()*1.15);fig.savefig(f"{PLOT_DIR}/chart4_droughts.png",dpi=150);plt.close();print("  Done: Chart 4")
def chart5(h2h):
    h2h["pct"]=h2h["Team_1_Wins"]/(h2h["Team_1_Wins"]+h2h["Team_2_Wins"]);h2h["margin"]=abs(h2h["Team_1_Wins"]-h2h["Team_2_Wins"])
    top=h2h.nlargest(10,"margin")[["Team_1","Team_2","Team_1_Wins","Team_2_Wins","pct","margin"]];top["label"]=top["Team_1"].str[:3]+" vs "+top["Team_2"].str[:3]
    fig,ax=plt.subplots(figsize=(12,7));y=range(len(top));cb=["#2166ac"if v<0.5 else"#d73027"if v>0.5 else"#ffffcc"for v in top["pct"]]
    ax.barh(y,top["margin"],color=cb,height=0.7)
    ax.set_yticks(y);ax.set_yticklabels(top["label"],fontsize=10);ax.set_xlabel("Win Margin (games)");ax.set_title("Top 10 NL H2H Rivalries",fontsize=15)
    for i,(_,r)in enumerate(top.iterrows()):ax.text(r["margin"]+2,i,f'{r["pct"]:.2f} ({r["Team_1_Wins"]}-{r["Team_2_Wins"]})',va="center",fontsize=8)
    ax.set_xlim(0,top["margin"].max()*1.2);fig.savefig(f"{PLOT_DIR}/chart5_h2h.png",dpi=150);plt.close();print("  Done: Chart 5")
if __name__=="__main__":
    print("NL Team Trends — Visualization Generator")
    hist,franchise,era,h2h=load_data();print(f"Data: {len(hist)} seasons, {len(franchise)} teams, {len(era)} eras, {len(h2h)} H2H pairs")
    print("Generating charts...");chart1(franchise,era);chart2(hist);chart3(hist);chart4(franchise);chart5(h2h)
    print(f"Charts saved to {PLOT_DIR}/")