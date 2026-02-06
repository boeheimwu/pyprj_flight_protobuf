import base64
#=====================
# trip=one way
trip_one_way_tfs_bef = "CBwQAhoqEgoyMDI2LTA3LTAxKABqDAgDEggvbS8wZnRreHIMCAMSCC9tLzA3ZGZrQAFIAXABggELCP___________wGYAQI"
# URL-safe Base64 decode
trip_one_way_tfs_bef_raw = base64.urlsafe_b64decode(trip_one_way_tfs_bef + "==")

trip_one_way_d1_bef = b"2026-07-01"
trip_one_way_d1_aft = b"2026-09-03"

assert len(trip_one_way_d1_bef) == len(trip_one_way_d1_aft)

if trip_one_way_d1_bef not in trip_one_way_tfs_bef_raw:
    raise ValueError("找不到one_way_d1原始日期")

# 等長替換
trip_one_way_tfs_aft_raw = trip_one_way_tfs_bef_raw.replace(trip_one_way_d1_bef, trip_one_way_d1_aft, 1)

# 再 encode 回 URL-safe Base64（不補 padding）
trip_one_way_tfs_aft = base64.urlsafe_b64encode(trip_one_way_tfs_aft_raw).decode().rstrip("=")
#=====================
# trip=round trip
trip_round_trip_tfs_bef = "CBwQAhoqEgoyMDI2LTA3LTA1KABqDAgDEggvbS8wZnRreHIMCAMSCC9tLzA3ZGZrGioSCjIwMjYtMDctMTAoAGoMCAMSCC9tLzA3ZGZrcgwIAxIIL20vMGZ0a3hAAUgBcAGCAQsI____________AZgBAQ"
# URL-safe Base64 decode
trip_round_trip_tfs_bef_raw = base64.urlsafe_b64decode(trip_round_trip_tfs_bef + "==")

trip_round_trip_d1_bef = b"2026-07-05"
trip_round_trip_d2_bef = b"2026-07-10"
trip_round_trip_d1_aft = b"2026-10-09"
trip_round_trip_d2_aft = b"2026-10-13"

assert len(trip_round_trip_d1_bef) == len(trip_round_trip_d1_aft)
assert len(trip_round_trip_d2_bef) == len(trip_round_trip_d2_aft)

if trip_round_trip_d1_bef not in trip_round_trip_tfs_bef_raw:
    raise ValueError("找不到round_trip_d1日期")
if trip_round_trip_d2_bef not in trip_round_trip_tfs_bef_raw:
    raise ValueError("找不到round_trip_d2日期")

# 等長替換
trip_round_trip_tfs_aft_raw = trip_round_trip_tfs_bef_raw.replace(trip_round_trip_d1_bef, trip_round_trip_d1_aft, 1).replace(trip_round_trip_d2_bef, trip_round_trip_d2_aft, 1)

# 再 encode 回 URL-safe Base64（不補 padding）
trip_round_trip_tfs_aft = base64.urlsafe_b64encode(trip_round_trip_tfs_aft_raw).decode().rstrip("=")

#=====================
# trip=Multi-city
trip_multi_city_tfs_bef = "CBwQAholEgoyMDI2LTA4LTA3KABqDAgDEggvbS8wZnRreHIHCAESA0hORBooEgoyMDI2LTA4LTExagwIAxIIL20vMDdkZmtyDAgDEggvbS8wZnRreEABSAFwAYIBCwj___________8BmAED"
# URL-safe Base64 decode
trip_multi_city_tfs_bef_raw = base64.urlsafe_b64decode(trip_multi_city_tfs_bef + "==")

trip_multi_city_d1_bef = b"2026-08-07"
trip_multi_city_d2_bef = b"2026-08-11"
trip_multi_city_d1_aft = b"2026-11-15"
trip_multi_city_d2_aft = b"2026-11-19"

assert len(trip_multi_city_d1_bef) == len(trip_multi_city_d1_aft)
assert len(trip_multi_city_d2_bef) == len(trip_multi_city_d2_aft)

if trip_multi_city_d1_bef not in trip_multi_city_tfs_bef_raw:
    raise ValueError("找不到multi_city_d1日期")
if trip_multi_city_d2_bef not in trip_multi_city_tfs_bef_raw:
    raise ValueError("找不到multi_city_d2日期")

# 等長替換
trip_multi_city_tfs_aft_raw = trip_multi_city_tfs_bef_raw.replace(trip_multi_city_d1_bef, trip_multi_city_d1_aft, 1).replace(trip_multi_city_d2_bef, trip_multi_city_d2_aft, 1)

# 再 encode 回 URL-safe Base64（不補 padding）
trip_multi_city_tfs_aft = base64.urlsafe_b64encode(trip_multi_city_tfs_aft_raw).decode().rstrip("=")

#=====================
table_rows = ""

# 建立 table row :: Part1
table_rows += f"""
            <tr style='vertical-align:top;'>
                <td><details><summary>one_way</summary> 
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:200px;">{trip_one_way_tfs_bef}</td></tr>
                    </table></details>
                </td>
                <td>{trip_one_way_d1_bef} </td>
                <td>{trip_one_way_d1_aft}</td>
                <td>
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:300px;"><sup>（<a href="https://www.google.com/travel/flights/search?tfs={trip_one_way_tfs_aft}" target="_blank">*</a>）</sup>https://www.google.com/travel/flights/search?tfs={trip_one_way_tfs_aft}</td></tr>
                    </table>
                </td>
            </tr>
        """
# 建立 table row :: Part2
table_rows += f"""
            <tr style='vertical-align:top;'>
                <td><details><summary>round_trip</summary> 
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:200px;">{trip_round_trip_tfs_bef}</td></tr>
                    </table></details>
                </td>
                <td>{trip_round_trip_d1_bef}~{trip_round_trip_d2_bef}</td>
                <td>{trip_round_trip_d1_aft}~{trip_round_trip_d2_aft}</td>
                <td>
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:300px;"><sup>（<a href="https://www.google.com/travel/flights/search?tfs={trip_round_trip_tfs_aft}" target="_blank">*</a>）</sup>https://www.google.com/travel/flights/search?tfs={trip_round_trip_tfs_aft}</td></tr>
                    </table>
                </td>
            </tr>
        """
# 建立 table row :: Part3
table_rows += f"""
            <tr style='vertical-align:top;'>
                <td><details><summary>multi_city</summary> 
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:200px;">{trip_multi_city_tfs_bef}</td></tr>
                    </table></details>
                </td>
                <td>{trip_multi_city_d1_bef}~{trip_multi_city_d2_bef}</td>
                <td>{trip_multi_city_d1_aft}~{trip_multi_city_d2_aft}</td>
                <td>
                    <table border="1" style="table-layout: fixed">
                    <tr><td style="width:300px;"><sup>（<a href="https://www.google.com/travel/flights/search?tfs={trip_multi_city_tfs_aft}" target="_blank">*</a>）</sup>https://www.google.com/travel/flights/search?tfs={trip_multi_city_tfs_aft}</td></tr>
                    </table>
                </td>
            </tr>
        """

# 建立完整 HTML
html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>RenewDate</title>
    </head>
    <body>
        <table border="1">
            <tr>
                <th>template</th>
                <th>bef_date</th>
                <th>aft_date</th>
                <th>change_str</th>
            </tr>
            {table_rows}
        </table>
    </body>
    </html>
    """
# 寫入 HTML 檔案
with open("bef_vs_aft.html", "w", encoding="utf-8") as f:
    f.write(html_content)
    
