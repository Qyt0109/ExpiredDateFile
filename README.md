# ExpiredDateFile
Tạo file license được mã hoá chứa thông tin về hạn sử dụng của một chương trình.

## Các file chương trình:
- rsa.py chứa các hàm liên quan tới mã hoá, giải mã thông tin sử dụng hệ mật mã khoá công khai RSA.
- license.py chứa các hàm tạo, đọc file chứa thông tin về cặp khoá RSA (trong ứng dụng thực tế, xin hãy lưu ý giữ các file này một cách bí mật), hàm đặt, đọc thời gian hết hạn vào file license.
- main.py là file chương trình chính, đây sẽ là ví dụ cơ bản để bạn có thể tự tạo ra những ứng dụng tương tự, áp dụng hướng đi của project này.

## Các file khác:
- private_key.pem, public_key.pem chứa thông tin về cặp khoá RSA.
- license chứa thông tin về ngày hết hạn, thông tin chứa trong file này đã được mã hoá.
- requirements.txt chứa thông tin về các module (thư viện) Python được sử dụng trong project. Bạn có thể sử dụng lệnh ```console pip install -r requirements.txt``` để tải xuống các gói cần thiết vào môi trường lập trình.
