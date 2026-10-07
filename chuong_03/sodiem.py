import csv
import io
from flask import (
    Flask,
    request,
    redirect,
    abort,
    make_response,
    jsonify,
    url_for,
    markupsafe
)

app = Flask(__name__)
app.json.ensure_ascii = False  # Bắt buộc: Cấu hình JSON hiển thị tiếng Việt có dấu[cite: 2, 3]

# -----------------------------------------------------------------------------
# CÂU 0.1 - 0.2: DỮ LIỆU MẪU[cite: 3]
# -----------------------------------------------------------------------------
STUDENTS = {
    "23T1020001": {"name": "Nguyễn Văn An", "lop": "K47A", "scores": {"PMMNM": 8.5, "CSDL": 7.0, "MMT": 9.0}},
    "23T1020002": {"name": "Trần Thị Bình", "lop": "K47A", "scores": {"PMMNM": 6.0, "CSDL": 5.5, "MMT": 7.0}},
    "23T1020003": {"name": "Lê Hoàng Cường", "lop": "K47B", "scores": {"PMMNM": 9.5, "CSDL": 9.0}},
    "23T1020004": {"name": "Phạm Minh Dũng", "lop": "K47B", "scores": {"PMMNM": 4.0, "CSDL": 3.5, "MMT": 5.0}},
    "23T1020005": {"name": "Hoàng Thu Hà", "lop": "K47A", "scores": {}},
    "23T1020006": {"name": "Võ Quốc Khánh", "lop": "K47C", "scores": {"PMMNM": 7.5, "MMT": 8.0}},
}

# -----------------------------------------------------------------------------
# CÂU 0.3 - 0.4: HÀM PHỤ VÀ KHUNG TRANG (LAYOUT)[cite: 4]
# -----------------------------------------------------------------------------
def average(scores):
    """Trung bình cộng, làm tròn 2 chữ số; dict rỗng -> None."""[cite: 4]
    if not scores:
        return None
    vals = list(scores.values())
    return round(sum(vals) / len(vals), 2)

def rank(avg):
    """Xếp loại dựa trên điểm trung bình."""[cite: 4]
    if avg is None:
        return "Chưa có điểm"
    if avg >= 8.5:
        return "Giỏi"
    if avg >= 7.0:
        return "Khá"
    if avg >= 5.0:
        return "Trung bình"
    return "Yếu"

def student_summary(mssv):
    """Dict thông tin tổng hợp của sinh viên."""[cite: 4]
    student = STUDENTS[mssv]
    avg = average(student["scores"])
    return {
        "mssv": mssv,
        "name": student["name"],
        "lop": student["lop"],
        "scores": student["scores"],
        "average": avg,
        "rank": rank(avg)
    }

def layout(title, body):
    """Khung HTML chung, sử dụng escape() và url_for()."""[cite: 2, 4]
    escaped_title = markupsafe.escape(title)
    
    home_url = url_for('home')
    students_url = url_for('student_list')
    search_url = url_for('search')
    
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>{escaped_title} - Sổ điểm</title>
</head>
<body>
    <nav>
        <a href="{home_url}">Trang chủ</a> | 
        <a href="{students_url}">Sinh viên</a> | 
        <a href="{search_url}">Tìm kiếm</a>
    </nav>
    <hr>
    <div>
        {body}
    </div>
</body>
</html>"""

# -----------------------------------------------------------------------------
# PHẦN 1: GIAO DIỆN WEB (CÂU 1 - 6)[cite: 1, 5, 6, 7, 8]
# -----------------------------------------------------------------------------
@app.route("/")
def home():
    """Câu 1: Trang chủ"""[cite: 5]
    total_students = len(STUDENTS)
    classes = set(s["lop"] for s in STUDENTS.values())
    total_classes = len(classes)
    
    students_link = url_for('student_list')
    api_link = url_for('api_student_list')
    
    body = f"""
    <h1>Tổng quan hệ thống</h1>
    <p>Tổng số sinh viên: <strong>{total_students}</strong></p>
    <p>Số lớp (không trùng): <strong>{total_classes}</strong></p>
    <p>
        <a href="{students_link}">Xem danh sách sinh viên (Web)</a> | 
        <a href="{api_link}">API Danh sách sinh viên (JSON)</a>
    </p>
    """
    return layout("Trang chủ", body)

@app.route("/students")
def student_list():
    """Câu 2: Danh sách sinh viên & lọc theo lớp"""[cite: 5]
    lop_filter = request.args.get("lop", "").strip()
    
    all_classes = sorted(list(set(s["lop"] for s in STUDENTS.values())))
    
    all_url = url_for('student_list')
    filter_bar_items = [f'<a href="{all_url}">Tất cả</a>']
    for c in all_classes:
        c_url = url_for('student_list', lop=c)
        filter_bar_items.append(f'<a href="{c_url}">{markupsafe.escape(c)}</a>')
    filter_bar_html = " | ".join(filter_bar_items)
    
    filtered_students = []
    for mssv in STUDENTS:
        info = student_summary(mssv)
        if lop_filter:
            if info["lop"].lower() == lop_filter.lower():
                filtered_students.append(info)
        else:
            filtered_students.append(info)
            
    if not filtered_students:
        table_body = "<p>Không có sinh viên phù hợp.</p>"
    else:
        rows = []
        for s in filtered_students:
            detail_url = url_for('student_detail', mssv=s["mssv"])
            avg_str = str(s["average"]) if s["average"] is not None else "-"
            
            row = f"""<tr>
                <td><a href="{detail_url}">{markupsafe.escape(s["mssv"])}</a></td>
                <td>{markupsafe.escape(s["name"])}</td>
                <td>{markupsafe.escape(s["lop"])}</td>
                <td>{markupsafe.escape(avg_str)}</td>
                <td>{markupsafe.escape(s["rank"])}</td>
            </tr>"""
            rows.append(row)
            
        table_body = f"""
        <table border="1" cellpadding="5" cellspacing="0">
            <thead>
                <tr>
                    <th>MSSV</th><th>Họ tên</th><th>Lớp</th><th>Điểm TB</th><th>Xếp loại</th>
                </tr>
            </thead>
            <tbody>{"".join(rows)}</tbody>
        </table>"""
        
    body = f"""
    <h1>Danh sách sinh viên</h1>
    <p>Thanh lọc theo lớp: {filter_bar_html}</p>
    {table_body}
    """
    return layout("Danh sách sinh viên", body)

@app.route("/students/<mssv>")
def student_detail(mssv):
    """Câu 3: Chi tiết sinh viên"""[cite: 6]
    if mssv not in STUDENTS:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")
        
    info = student_summary(mssv)
    lop_url = url_for('student_list', lop=info["lop"])
    export_url = url_for('export_csv', mssv=mssv)
    short_link_url = url_for('short_student_detail', mssv=mssv)
    
    avg_str = str(info["average"]) if info["average"] is not None else "-"
    
    scores_rows = []
    for course, score in info["scores"].items():
        scores_rows.append(f"<tr><td>{markupsafe.escape(course)}</td><td>{markupsafe.escape(str(score))}</td></tr>")
        
    scores_table = f"""
    <table border="1" cellpadding="5" cellspacing="0">
        <thead><tr><th>Học phần</th><th>Điểm</th></tr></thead>
        <tbody>{"".join(scores_rows) if scores_rows else '<tr><td colspan="2">Chưa có điểm học phần nào</td></tr>'}</tbody>
    </table>"""
    
    body = f"""
    <h1>Thông tin sinh viên: {markupsafe.escape(info["name"])}</h1>
    <p><strong>MSSV:</strong> {markupsafe.escape(info["mssv"])}</p>
    <p><strong>Lớp:</strong> <a href="{lop_url}">{markupsafe.escape(info["lop"])}</a></p>
    <p><strong>Điểm TB:</strong> {markupsafe.escape(avg_str)}</p>
    <p><strong>Xếp loại:</strong> {markupsafe.escape(info["rank"])}</p>
    
    <h3>Bảng điểm chi tiết</h3>
    {scores_table}
    
    <p style="margin-top: 15px;">
        <a href="{export_url}">Tải bảng điểm (CSV)</a> | 
        <span>Link rút gọn: <code>{short_link_url}</code></span>
    </p>
    """
    return layout(f"Sinh viên {info['name']}", body)

@app.route("/sv/<mssv>")
def short_student_detail(mssv):
    """Câu 4: Redirect 301 sang URL chi tiết"""[cite: 6]
    target_url = url_for('student_detail', mssv=mssv)
    return redirect(target_url, code=301)

@app.route("/students/<mssv>/export")
def export_csv(mssv):
    """Câu 5: Xuất file CSV"""[cite: 7]
    if mssv not in STUDENTS:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")
        
    scores = STUDENTS[mssv]["scores"]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["hoc_phan", "diem"])
    for course, score in scores.items():
        writer.writerow([course, score])
        
    response = make_response(output.getvalue())
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    response.headers["Content-Disposition"] = f"attachment; filename=diem_{mssv}.csv"
    return response

@app.route("/search")
def search():
    """Câu 6: Tìm kiếm an toàn (Chống XSS)"""[cite: 8]
    q = request.args.get("q", "").strip()
    escaped_q = markupsafe.escape(q)
    
    results = []
    if q:
        q_lower = q.lower()
        for mssv, data in STUDENTS.items():
            if q_lower in mssv.lower() or q_lower in data["name"].lower():
                results.append(student_summary(mssv))
                
    results_html = ""
    if q:
        if results:
            items = []
            for r in results:
                detail_url = url_for('student_detail', mssv=r["mssv"])
                items.append(f'<li><a href="{detail_url}">{markupsafe.escape(r["mssv"])} - {markupsafe.escape(r["name"])} ({markupsafe.escape(r["lop"])})</a></li>')
            results_html = f"<p>Tìm thấy {len(results)} kết quả cho “{escaped_q}”:</p><ul>{''.join(items)}</ul>"
        else:
            results_html = f"<p>Tìm thấy 0 kết quả cho “{escaped_q}”.</p>"
            
    body = f"""
    <h1>Tìm kiếm sinh viên</h1>
    <form method="GET" action="{url_for('search')}">
        <input type="text" name="q" value="{escaped_q}" placeholder="Nhập tên hoặc MSSV...">
        <button type="submit">Tìm kiếm</button>
    </form>
    {results_html}
    """
    return layout("Tìm kiếm", body)

# -----------------------------------------------------------------------------
# PHẦN 2: API JSON (CÂU 7 - 8)[cite: 1, 9, 10]
# -----------------------------------------------------------------------------
@app.route("/api/students", methods=["GET"])
def api_student_list():
    """Câu 7: API đọc danh sách sinh viên"""[cite: 9]
    lop_param = request.args.get("lop")
    min_avg_param = request.args.get("min_avg")
    
    min_avg_val = None
    if min_avg_param is not None:
        try:
            min_avg_val = float(min_avg_param)
        except ValueError:
            abort(400, description="Tham số min_avg phải là số thực hợp lệ.")
            
    res = []
    for mssv in STUDENTS:
        info = student_summary(mssv)
        
        if lop_param is not None:
            if info["lop"].lower() != lop_param.strip().lower():
                continue
                
        if min_avg_val is not None:
            if info["average"] is None or info["average"] < min_avg_val:
                continue
                
        res.append(info)
        
    return jsonify(res)

@app.route("/api/students/<mssv>", methods=["GET"])
def api_student_detail(mssv):
    if mssv not in STUDENTS:
        abort(404, description=f"Không có sinh viên với MSSV = {mssv}.")
    return jsonify(student_summary(mssv))

@app.route("/api/students/<mssv>/scores/<course>", methods=["GET", "PUT", "DELETE", "POST"])
def api_course_score(mssv, course):
    """Câu 8: Quản lý điểm học phần"""[cite: 10]
    course_code = course.upper()  # Luôn lưu chữ HOA[cite: 10]
    
    if mssv not in STUDENTS:
        abort(404, description=f"Không tìm thấy sinh viên với MSSV = {mssv}.")
        
    scores = STUDENTS[mssv]["scores"]
    
    if request.method == "POST":
        abort(405, description="Phương thức POST không được hỗ trợ trên endpoint này.")
        
    if request.method == "GET":
        if course_code not in scores:
            abort(404, description=f"Học phần {course_code} chưa có điểm.")
        return jsonify({
            "mssv": mssv,
            "course": course_code,
            "score": scores[course_code]
        })
        
    if request.method == "PUT":
        score_param = request.args.get("score")
        if score_param is None:
            abort(400, description="Thiếu tham số score.")
            
        try:
            score_val = float(score_param)
        except ValueError:
            abort(400, description="Tham số score phải là số thực hợp lệ.")
            
        if not (0 <= score_val <= 10):
            abort(400, description="Điểm phải nằm trong khoảng [0, 10].")
            
        is_new = course_code not in scores
        scores[course_code] = score_val
        
        updated_summary = student_summary(mssv)
        response_data = {
            "mssv": mssv,
            "course": course_code,
            "score": score_val,
            "average": updated_summary["average"]
        }
        
        if is_new:
            res = make_response(jsonify(response_data), 201)
            res.headers["Location"] = url_for('api_course_score', mssv=mssv, course=course_code)
            return res
        else:
            return jsonify(response_data), 200
            
    if request.method == "DELETE":
        if course_code not in scores:
            abort(404, description=f"Học phần {course_code} chưa có điểm để xoá.")
        del scores[course_code]
        return "", 204

# -----------------------------------------------------------------------------
# PHẦN 3: XỬ LÝ LỖI THỐNG NHẤT (CÂU 9)[cite: 1, 11]
# -----------------------------------------------------------------------------
ERROR_TITLES = {
    400: "Dữ liệu không hợp lệ",
    404: "Không tìm thấy",
    405: "Phương thức không được hỗ trợ"
}

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
def handle_error(error):
    code = error.code
    title = ERROR_TITLES.get(code, "Lỗi hệ thống")
    detail = getattr(error, 'description', str(error))
    
    # Nếu URL bắt đầu bằng /api/ -> Trả về JSON[cite: 11]
    if request.path.startswith("/api/"):
        return jsonify({"error": title, "detail": detail}), code
        
    # URL khác -> Trả về trang HTML[cite: 11]
    body = f"""
    <h1>{code} - {markupsafe.escape(title)}</h1>
    <p>{markupsafe.escape(detail)}</p>
    <p><a href="{url_for('home')}">Quay lại Trang chủ</a></p>
    """
    return layout(f"Lỗi {code}", body), code

if __name__ == "__main__":
    app.run(port=8000, debug=True)
