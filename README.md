hackerearth
===========

Nơi dành cho anh em coder học tập, chia sẻ, cùng nhau phát triển. <br>
Mình tổng hợp bài tập lấy đề bài từ trang [**hackerearth.com**](http://www.hackerearth.com/problems/). <br>
Đây là trang học lập trình rất tốt để luyện tư duy cũng như khả năng code, cho phép giải quyết vấn đề bằng nhiều ngôn ngữ lập trình khác nhau! <br> 
Mình mong muốn mọi người học lập trình sẽ cùng nhau làm những bài tập trong này, chia sẻ, góp ý cho nhau về lời giải để có được bài code đẹp, tối ưu nhất có thể! <br>
Hy vọng anh em tham gia nhiệt tình :D 
##

***Note:*** Do mình mới bắt đầu học lập trình với ngôn ngữ Python nên mình xin chia sẻ một số bài mình đã làm trong thư mục Python, mong anh em góp ý! Hy vọng sẽ có nhiều người chia sẻ ở các ngôn ngữ khác nữa!

#### Đề bài
### 1. The best Internet Browser
Một trình duyệt thông minh có thể đoán được những nguyên âm (u, e, o, a, i) còn thiếu từ địa chỉ mà người dùng nhập vào. <br>
Với trình duyệt này, khi muốn truy cập vào một website:
- Bạn không cần nhập **www.**
- Bạn phải nhập **.com**
- Tình duyệt có thể đoán được tất cả **nguyên âm** trong tên của website (trừ ".com")
=> Điều này giúp truy cập vào một trang web nhanh chóng và dễ dàng hơn.

Yêu cầu đề bài:
- input:
    
        Dòng đầu tiên sẽ là số lần nhập vào (n).
        Tiếp theo sẽ nhập n tên đầy đủ của trang web (www.google.com) tương ứng với n dòng
        Mọi trang web nhập vào đều bắt đầu bằng www. và có phần mở rộng là .com

- output:
    
        Hiển thị tỉ lệ giữa số chữ cái phải nhập vào trên tên đầy đủ của trang web.

Ví dụ:

    input:
    2
    www.google.com
    www.hackerearth.com
###
    output:
    7/14
    11/19



Yêu cầu về code:

    Time Limit: 1 sec(s) for each input file.
    Memory Limit: 256 MB
    Source Limit: 1024 KB
    Scoring: Score is assigned in case any testcase passes.

