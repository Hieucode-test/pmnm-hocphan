# pmnm-hocphan
# Kho Lưu Trữ Học Phần Phần Mềm Mã Nguồn Mở

## Thông Tin Sinh Viên
- **Họ và tên:** Ngô Thành Hiếu
- **Mã sinh viên:** 23T1020172
- **Lớp:** K47B

---

## Lý Do Tôi Muốn Học Về Phần Mềm Mã Nguồn Mở

Tôi muốn học về phần mềm mã nguồn mở (OSS) vì đây là cánh cửa mở ra tư duy lập trình hiện đại và tinh thần hợp tác cộng đồng. Việc tiếp cận mã nguồn mở giúp tôi không chỉ hiểu rõ cơ chế hoạt động đằng sau các công cụ công nghệ phổ biến mà còn học hỏi được tư duy thiết kế, chuẩn viết mã và cách giải quyết vấn đề từ hàng triệu nhà phát triển giỏi trên toàn thế giới. Bên cạnh đó, học về phần mềm mã nguồn mở cho tôi cơ hội thực hành quản lý phiên bản, làm việc nhóm qua các nền tảng như GitHub/GitLab và hiểu sâu hơn về các khía cạnh pháp lý như bản quyền, giấy phép phần mềm. Đây là nền tảng vững chắc giúp tôi chủ động tích hợp, tùy biến các thư viện mã nguồn mở vào dự án thực tế, từ đó nâng cao tay nghề lập trình và mở rộng cơ hội phát triển sự nghiệp trong tương lai.

---

## 5 Phần Mềm Mã Nguồn Mở Tôi Đang Sử Dụng Hằng Ngày

| STT | Tên phần mềm | Công dụng chính | Giấy phép (License) |
|---|---|---|---|
| 1 | **Visual Studio Code** | Trình soạn thảo mã nguồn | [MIT License](https://github.com/microsoft/vscode/blob/main/LICENSE.txt) *(Bản dựng mã nguồn mở Code - OSS)* |
| 2 | **Git** | Hệ thống quản lý phiên bản phân tán | [GNU General Public License v2.0 (GPL-2.0)](https://git-scm.com/site/about/license) |
| 3 | **Mozilla Firefox** | Trình duyệt web | [Mozilla Public License 2.0 (MPL-2.0)](https://www.mozilla.org/en-US/MPL/2.0/) |
| 4 | **VLC Media Player** | Trình phát đa phương tiện | [GNU Lesser General Public License v2.1 (LGPL-2.1)](https://www.videolan.org/legal.html) |
| 5 | **7-Zip** | Phần mềm nén và giải nén dữ liệu | [GNU Lesser General Public License (LGPL)](https://www.7-zip.org/license.txt) |
## BÀI 1.2: BÁO CÁO PHÂN TÍCH DỰ ÁN MÃ NGUỒN MỞ RẼ NHÁNH (FORK)

**Tên đề tài:** Phân tích mâu thuẫn cộng đồng và sự hình thành dự án MariaDB từ MySQL

### 1. Mở đầu
MySQL từng là hệ quản trị cơ sở dữ liệu quan hệ mã nguồn mở phổ biến nhất thế giới, làm nền tảng cho hàng triệu website và ứng dụng. Tuy nhiên, năm 2009, một thương vụ mua bán sáp nhập lớn trong ngành công nghệ đã tạo ra làn sóng lo ngại sâu sắc trong cộng đồng nhà phát triển, dẫn đến cuộc rẽ nhánh (fork) lịch sử để tạo ra MariaDB. Đây là một trong những ví dụ điển hình nhất về mâu thuẫn giữa lợi ích doanh nghiệp và định hướng của cộng đồng mã nguồn mở.

### 2. Nguyên nhân và Bối cảnh mâu thuẫn
Ban đầu, MySQL được phát triển bởi công ty MySQL AB (Thụy Điển). Năm 2008, Sun Microsystems mua lại MySQL AB. Tuy nhiên, chỉ một năm sau đó (2009), tập đoàn Oracle thông báo thâu tóm Sun Microsystems. 

Sự kiện Oracle sở hữu MySQL đã dấy lên làn sóng phản đối mạnh mẽ từ cộng đồng. Oracle vốn nổi tiếng với hệ quản trị cơ sở dữ liệu thương mại khép kín và đắt đỏ. Cộng đồng lo ngại Oracle sẽ triệt hạ hoặc thương mại hóa MySQL để bảo vệ sản phẩm cốt lõi của họ. Mâu thuẫn về mặt triết lý xuất hiện: cộng đồng muốn giữ MySQL hoàn toàn tự do và minh bạch, trong khi việc Oracle nắm giữ bản quyền và quyền ra quyết định khiến tính "mở" của dự án bị đe dọa nghiêm trọng.

### 3. Quá trình rẽ nhánh và sự ra đời của MariaDB
Nhận thấy nguy cơ tiềm ẩn, Michael "Monty" Widenius — nhà sáng lập gốc của MySQL — đã quyết định rời khỏi Oracle. Để bảo vệ tương lai của hệ quản trị cơ sở dữ liệu tự do này, Monty cùng các kỹ sư nòng cốt đã thực hiện rẽ nhánh mã nguồn của MySQL để tạo ra một dự án mới mang tên **MariaDB** vào năm 2009.

MariaDB được thiết kế để thay thế hoàn toàn (drop-in replacement) cho MySQL, nghĩa là người dùng có thể chuyển từ MySQL sang MariaDB mà không cần sửa đổi ứng dụng. Để đảm bảo mâu thuẫn sở hữu không lặp lại, cộng đồng đã thành lập **MariaDB Foundation** — một tổ chức phi lợi nhuận độc lập chịu trách nhiệm quản trị dự án, đảm bảo mã nguồn luôn tuân thủ giấy phép GPLv2 và không bị chi phối bởi bất kỳ tập đoàn đơn lẻ nào.

### 4. Tác động và Bài học kinh nghiệm
Cuộc rẽ nhánh này đã làm thay đổi bản đồ công nghệ. MariaDB nhanh chóng nhận được sự ủng hộ mạnh mẽ từ cộng đồng. Nhiều hệ điều hành Linux lớn như Red Hat, CentOS, Debian và Arch Linux đã quyết định loại bỏ MySQL để chọn MariaDB làm hệ quản trị cơ sở dữ liệu mặc định. Các gã khổng lồ công nghệ như Wikipedia hay Google cũng dịch chuyển một phần lớn hệ thống sang MariaDB.

Trường hợp của MySQL và MariaDB mang lại bài học đắt giá về quản trị mã nguồn mở:
- **Tầm quan trọng của tính độc lập:** Sự sống còn của một dự án mã nguồn mở phụ thuộc vào niềm tin của cộng đồng chứ không chỉ sở hữu pháp lý.
- **Sức mạnh của cộng đồng:** Khi doanh nghiệp cố tình khép kín dự án, cộng đồng hoàn toàn có quyền lực và năng lực rẽ nhánh để bảo vệ các giá trị cốt lõi của phần mềm tự do.
