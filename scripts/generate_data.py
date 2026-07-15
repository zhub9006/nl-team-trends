"""Generate NL historical performance CSV data files."""
import os

def wcsv(path, headers, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = __import__("csv").writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print("Written " + path + " (" + str(len(rows)) + " rows)")

# Detailed year-by-year NL performance (1876-2025)
hdr = ["year","champion","champion_record","second_place","ws_opponent","ws_result","era","division_east","division_central","division_west","notes"]
rows = []
# 1876-1910
rows += [("1876","Chicago White Stockings","52-14","Boston","Not Played","Founding","Chicago","","","Inaugural; 8 teams"),("1877","Boston Red Stockings","42-18","Chicago","Not Played","Founding","Boston","","","2nd straight NL title"),("1878","Boston Red Stockings","41-19","Cincinnati","Not Played","Founding","Boston","","","3rd title in 4 yrs"),("1879","Providence Grays","59-25","Boston","Not Played","Founding","Providence","","","Only title for Providence"),("1880","Chicago White Stockings","67-17","Cincinnati","Not Played","Founding","Chicago","","","Return to form"),("1881","Chicago White Stockings","56-28","Providence","Not Played","Founding","Chicago","","","3rd in 4 yrs"),("1882","Chicago White Stockings","55-29","Providence","Not Played","Founding","Chicago","","","4th in 5 yrs"),("1883","Providence Grays","58-26","Boston","Not Played","Founding","Providence","","","2nd title"),("1884","Providence Grays","84-28","NY Mets (AA)","W","Founding","Providence","","","Pre-WS postseason"),("1885","Chicago White Stockings","87-25","Detroit","L","Founding","Chicago","","","1st WS attempt"),("1886","Chicago White Stockings","90-34","Detroit","L","Founding","Chicago","","","2nd straight WS loss"),("1887","Detroit Wolverines","79-45","Philadelphia","W","Founding","Detroit","","","1st Detroit pennant"),("1888","New York Giants","84-47","Washington (AA)","W","Founding","New York","","","1st NL pennant for NY Giants"),("1889","New York Giants","83-43","Boston","W","Founding","New York","","","Back-to-back"),("1890","Boston Beaneaters","88-44","Brooklyn (PL)","W","Founding","Boston","","","1890 many leagues"),("1891","Boston Beaneaters","87-51","New York","Not Played","Founding","Boston","","","3rd title")]