# ExpiredDateFile
Tạo file license được mã hoá chứa thông tin về hạn sử dụng của một chương trình.

## Các file chương trình:
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/rsa.py">rsa.py</a> chứa các hàm liên quan tới mã hoá, giải mã thông tin sử dụng hệ mật mã khoá công khai RSA với module (thư viện) <a href="https://cryptography.io">cryptography</a>.
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/license.py">license.py</a> chứa các hàm tạo, đọc file chứa thông tin về cặp khoá RSA (trong ứng dụng thực tế, xin hãy lưu ý giữ các file này một cách bí mật), hàm đặt, đọc thời gian hết hạn vào file license.
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/main.py">main.py</a> là file chương trình chính, đây sẽ là ví dụ cơ bản để bạn có thể tự tạo ra những ứng dụng tương tự, áp dụng hướng đi của project này.

## Các file khác:
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/private_key.pem">private_key.pem</a>, <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/public_key.pem">public_key.pem</a> chứa thông tin về cặp khoá RSA.
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/license">license</a> chứa thông tin về ngày hết hạn, thông tin chứa trong file này đã được mã hoá.
- <a href="https://github.com/Qyt0109/ExpiredDateFile/blob/main/requirements.txt">requirements.txt</a> chứa thông tin về các module (thư viện) Python được sử dụng trong project. Bạn có thể sử dụng lệnh ```console pip install -r requirements.txt``` để tải xuống các gói cần thiết vào môi trường lập trình.
