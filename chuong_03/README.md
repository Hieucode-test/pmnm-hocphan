# Bài tập tổng hợp Chương 3 - Sổ điểm

## 1. Danh sách Routes (`flask --app sodiem routes`)
Gồm 10 routes:
- api_course_score (/api/students/<mssv>/scores/<course>)
- api_student_detail (/api/students/<mssv>)
- api_student_list (/api/students)
- export_csv (/students/<mssv>/export)
- home (/)
- search (/search)
- short_student_detail (/sv/<mssv>)
- static (/static/<filename>)
- student_detail (/students/<mssv>)
- student_list (/students)

## 2. Kết quả kiểm thử cURL
- `$B/sv/23T1020001`: Trả về mã 301, Location `/students/23T1020001`
- `$B/students/23T1020001/export`: Trả về CSV kèm Content-Disposition attachment
- `$B/api/students?lop=k47a&min_avg=7`: Trả về JSON danh sách sinh viên phù hợp
- `$B/api/students?min_avg=abc`: Trả về 400 Bad Request JSON
- `$B/api/students/999`: Trả về 404 Not Found JSON
- `PUT $S/web?score=9`: Trả về 201 Created JSON kèm header Location
- `PUT $S/WEB?score=7.5`: Trả về 200 OK JSON
- `PUT $S/WEB?score=11`: Trả về 400 Bad Request JSON
- `DELETE $S/WEB`: Trả về 204 No Content
- `POST $S/WEB`: Trả về 405 Method Not Allowed (JSON)
- `POST $B/students`: Trả về 405 Method Not Allowed (HTML)

## 3. Câu hỏi ngắn
1. **Vì sao dùng được `request` trong `handle_error`?**
   Flask duy trì **Request Context** xuyên suốt vòng đời xử lý yêu cầu. Khi xảy ra lỗi và nhảy vào `@app.errorhandler`, Request Context vẫn tồn tại nên đối tượng `request` vẫn truy cập bình thường.

2. **Vì sao Câu 4 dùng 301 còn Câu 8 dùng 201 + Location?**
   - **301 (Moved Permanently):** Chuyển hướng vĩnh viễn từ link rút gọn sang URL chính thức.
   - **201 (Created) + Location:** Chuẩn RESTful API thông báo tạo mới tài nguyên thành công và trả về URL của tài nguyên vừa tạo.

3. **Thêm điểm rồi khởi động lại server, điểm đó còn không?**
   **Không còn.** Vì dữ liệu được lưu tạm thời trên bộ nhớ RAM (In-memory variable `STUDENTS`). Khi khởi động lại server, chương trình Python chạy lại và reset biến về ban đầu.
