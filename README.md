hackerearth
===========

Nơi dành cho anh em coder học tập, chia sẻ, cùng nhau phát triển. <br>
Mình tổng hợp bài tập lấy đề bài từ trang [**hackerearth.com**](http://www.hackerearth.com/problems/). <br>
Đây là trang học lập trình rất tốt để luyện tư duy cũng như khả năng code, cho phép giải quyết vấn đề bằng nhiều ngôn ngữ lập trình khác nhau! <br> 
Mình mong muốn mọi người học lập trình sẽ cùng nhau làm những bài tập trong này, chia sẻ, góp ý cho nhau về lời giải để có được bài code đẹp, tối ưu nhất có thể! <br>
Hy vọng anh em tham gia nhiệt tình :D 
##

***Note:*** Mọi người nên vào website ở trên đăng ký tài khoản rồi thử code ở trên web, chỉ khi submit thành công thì code của mình mới đúng cho mọi trường hợp và phù hợp với yêu cầu của code. Mình mới bắt đầu học lập trình với ngôn ngữ Python nên mình xin chia sẻ một số bài mình đã làm trong thư mục Python, mong anh em góp ý! Hy vọng sẽ có nhiều người chia sẻ ở các ngôn ngữ khác nữa! 

### Đề bài
#### 1. The best Internet Browser
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

#### 2. Small Factorials
Viết chương trình tính lũy thừa
Yêu cầu:
- input:

        Dòng đầu tiên là số lần nhập vào (n).
        n dòng tiếp theo là các số tự nhiên > 1

- outout:

        Hiển thị n dòng tương ứng với n kết quả của n số nhập vào

Ví dụ:

    input:
    4
    1
    2
    5
    3
###
    output:
    1
    2
    120
    6

#### 3. Karan and Even Numbers
#### 4. Roy and Profile Picture
Roy wants to change his profile picture on Facebook. Now Facebook has some restriction over the dimension of picture that we can upload.
Minimum dimension of the picture can be L x L, where L is the length of the side of square.
##### 
Now Roy has N photos of various dimensions.
Dimension of a photo is denoted as W x H
where W - width of the photo and H - Height of the photo
##### 
When any photo is uploaded following events may occur:
#####
[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.  <br>
[2] If width and height, both are large enough and <br>
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case. <br>
(b) else user is prompted to crop it. Print "CROP IT" in this case. <br>
##### 
(quotes are only for clarification)
##### 
Given L, N, W and H as input, print appropriate text as output.
##### 
Input:

        First line contains L.
        Second line contains N, number of photos.
        Following N lines each contains two space separated integers W and H.

Output:

        Print appropriate text for each photo in a new line.

Constraints:

        1 <= L,W,H <= 10000
        1 <= N <= 1000 


Sample Input 

        180
        3
        640 480
        120 300
        180 180

Sample Output 

        CROP IT
        UPLOAD ANOTHER
        ACCEPTED

#### 5. Gotta catch 'em all!
Little Arihant has always wanted to be the best Pokemon trainer in this world. And he thinks he has achieved his goal, so he wants to quickly go and meet Professor Oak and verify this fact. But like all Pokemon trainers, he has a weird habit, too. He catches Pokemons which can go through evolution to become a better one. After roaming in the Pokeworld for days, he has finally managed to catch k such Pokemons.
#### 
The way he can make a Pokemon go through evolution is NOT by making them fight battles, but by using an evolution stone. Since he has k Pokemons, he naturally needs k evolution stones for every one of them, as well.
#### 
Now it takes little Arihant one complete day, to use the evolution stone on one Pokemon. And for each Pokemon, he knows how many days will they take to evolute after the evolution stone has been used on them.
#### 
He will go to meet Professor Oak, the very next day, once all his Pokemons have gone through evolution. He can select the order of applying evolution stones as he likes, so he wants to do it in such a way that he gets to meet Professor Oak as soon as possible!
#### 
Input Format: <br>
The input has two lines. The first line will contain an integer k, which denotes the number of Pokemons. Then, a line with k integers follows, where the i-th integer denotes the number of days it takes for the i-th Pokemon to evolve.
####
Output Format: <br>
You need to print the earliest day when little Arihant can go meet Professor Oak.
#### 
Constraints:

        The days are numbered 1, 2, 3, 4, 5, 6...
        1 ≤ k ≤ 10^5.
        1 ≤ Number of days ≤ 10^6.

Sample Input 

        2
        3 1

Sample Output

        5

Explanation <br>
Here's how it happens:<br>
Day 1: He uses the evolution stone on the Pokemon which takes 3 days.<br>
Day 2: 3 days Pokemon's first day. He uses the evolution stone on the Pokemon which takes 1 day.<br>
Day 3: 3 days Pokemon's second day. 1 day Pokemon's first and final day. It goes through evolution.<br>
Day 4: 3 days Pokemon's third day. It goes through evolution. All Pokemons done with, he can go to Professor Oak, now.<br>
Day 5: He goes to Professor Oak.<br>

#### 6. Girlfriend's demands
Like most of the girlfriends, Ashima when asks for something, won’t stop until she gets that.
The way she gets that is by keep on repeating the same things again and again. Like if she wants chocolate, she will just keep on repeating “chocolate” again and again.
#### 
I have decided to answer to her demands as “Yes” or “No” by not delaying a lot. Otherwise, there would be a lot of repercussions. So, randomly at certain intervals, I just answer with “Yes” or “No” using the following rule, I will just select two integers a and b, if the element at the position a is same as the element as position b in the non-ending chant by Ashima, I will speak “Yes”, otherwise say “No”.
#### 
Your job is to find my side of the conversation given the name of the demand Ashima has and the random integers I picked.
#### 
Input:

        First line of the input contains a string S, the name of the item she is demanding.
        Next line contains an integer Q, the number of pairs of integers that used to say “Yes” or “No” to her. These pairs are given in order.
        Next Q line, each contains 2 integers, a and b. (1-based indexing)

Output:

        For each query, print “Yes” or “No” as described above.

Constraints:

        1 ≤ |S| ≤ 105
        1 ≤ Q ≤ 105
        1 ≤ a, b ≤ 1018


Sample Input

        vgxgp
        3
        2 4
        2 5
        7 14

Sample Output

        Yes
        No
        Yes

#### 7. Fizz Buzz Test
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. Print a new line after each string or number.

####8. Complete String
A string is said to be complete if it contains all the characters from a to z. Given a string, check if it complete or not.
#### 
Input

        First line of the input contains the number of strings N. It is followed by N lines each contains a single string.
#### 
Output

        For each test case print "YES" if the string is complete, else print "NO"

Constraints 

        1 <= N <= 10
        The length of the string is at max 100 and the string contains only the characters a to z
    
Sample Input

        3
        wyyga
        qwertyuioplkjhgfdsazxcvbnm
        ejuxggfsts

Sample Output

        NO
        YES
        NO

#### 9. Crazy kangaroo
Little Jhool is a world renowned kangaroo trainer. He's now living in Australia, and is training kangaroos for his research project on mobile soccer. (We don't know the connection, too.) Anyway, for the project to be completed he observes kangaroos for a lot of time - because he wants to figure out the hop count for various kangaroos he's training.
#### 
Now, he makes a kangaroo stand at the starting point, and lets him jump to the finishing point - given the hop count of that particular kangaroo, figure out the number of jumps he would take between the starting point to the ending point. Both the starting point and the ending points are inclusive.
#### 
Note: He will jump only to those positions which are multiples of M or hop count.
####
Input:

        First line contains number of test cases T. Next T lines contains three integers A, B and M separated by single space. A denoted the starting point, B the finishing point - and M, the hop count - the distance covered by that kangaroo in one jump.

Output:

        For each test case print the number of jumps the kangaroo had to make in the range [A, B] inclusive.

Constraints:

        1<=T<=100000
        1<=A<=B<=1012
        1<=M<=1012 
 
Sample Input

        3
        1 10 2
        5 10 3
        7 9 5

Sample Output

        5
        2
        0

#### 10. Life, the Universe, and Everything
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
#### 
Sample Input 

        1
        2
        88
        42
        99

Sample Output

        1
        2
        88

#### 11. Date With Avni 
Problem :
#### 
Bajirao is on a date with his girlfriend Avni. It is a romantic night and they are playing a game of words.
#### 
The rule of this game is that if Bajirao says a word such that no adjacent letters occurring in the word are same then he gets a kiss from her otherwise he gets a slap.

Input :

        The first line consists of T the number of test cases. The next T lines are such that each line consists of a single word spoken by Bajirao.

Output

        For every test case, on a new line print 'KISS' if Bajirao gets a kiss and 'SLAP' if Bajirao gets a slap.

Constraints :

        1<=T<=100
        2<=Length of Word spoken by Bajirao<=100
        The input word will comprise only of lower case English alphabets (a-z).
#### 
Sample Input 

        2
        remember
        occurring

Sample Output 

        KISS
        SLAP

#### 12. Minimal Combinatorial
Given two integers - n and r, your task is to calculate the combinatorial nCr.
nCr = n! / r! (n-r)! <br>
The caveat is that you have to write code to do this calculation in minimum number of characters.
#### 
UPDATE: The testcases for this problem have been fixed. Please try submitting your solution again.
#### 
Input

        The first line will be number of testcases T. Then T lines follow, each containing two positive integers - n and r.

output

        Print T lines, each line containing the value of nCr.

Constraints

        1 <= T <= 100
        1 <= r <= n <= 1000

You can assume that the value nCr will fit into a signed 64 bit integer.
#### 
Scoring

        If your program passes all the testcases, the score will be assigned according to the following formula:
        num_chars = length of source code
        Score = (1000 - num_chars) / 10
#### 
You can understand that you have to reach as close to 100 as possible. Have fun :)
#### 
Sample Input 

        1
        100 10

Sample Output 

        17310309456440

#### 13. What is the string made of?
You are given a string, which contains entirely of decimal digits (0-9). Each digit is made of a certain number of dashes, as shown in the image below. For instance 1 is made of 2 dashes, 8 is made of 7 dashes and so on.
#### 
You have to write a function that takes this string message as an input and returns a corresponding value in terms of a number. This number is the count of dashes in the string message.
####
Note:
####
0 consists of 6 dashes, 1 consists of 2 dashes, 2 consists of 5 dashes, 3 consists of 5 dashes, 4 consists of 4 dashes, 5 consists of 5 dashes, 6 consists of 6 dashes, 7 consists of 3 dashes [though the figure shows that 7 consists of 4 dashes but due to minor mistake in the problem please write your solution assuming 7 consists of 3 dashes], 8 consists of 7 dashes, 9 consists of 6 dashes.
####
Constraints

    String message will contain at least one digit, but not more than 100
    Each character in code will be a digit ('0'-'9').

Sample Input 

        12134

Sample Output 

        18

#### 14. Password
Danny has a possible list of passwords of Manny's facebook account. All passwords length is odd. But Danny knows that Manny is a big fan of palindromes. So, his password and reverse of his password both should be in the list.
#### 
You have to print the length of Manny's password and it's middle character.
#### 
Note : The solution will be unique.
#### 
INPUT

        The first line of input contains the integer N, the number of possible passwords.
        Each of the following N lines contains a single word, its length being an odd number greater than 2 and lesser than 14. All characters are lowercase letters of the English alphabet.

OUTPUT

        The first and only line of output must contain the length of the correct password and its central letter.

CONSTRAINTS

        1 ≤ N ≤ 100
Sample Input 

        4
        abc
        def
        feg
        cba

Sample Output 

        3 b

#### 15. Hell of a Day
Problem
#### 
Bajirao wants to protect Guruji and for that he has arranged a special force of expert officers. But Baba is also an intelligent enemy of Bajirao and he has also arranged a bunch of expert shooters from foreign countries.
#### 
Every man has some experience points. In this scenario Bajirao's men have even experience points and Baba's men have odd experience points.
#### 
Now, Bajirao's strategy is to place his men in ascending order so that if enemy is going to attack then the more experienced men can easily takeover the enemy.
#### 
But Baba also has a stratergy. Baba will send his force in a descending order of experience points so that their motive of killing Guruji will be achieved , as, even if the more experienced ones die the less experienced ones can reach inside and kill Guruji.
#### 
Now, you have been given an array of experience points of men and you have to find the men belonging to Bajirao's Force and Baba's Force and print their experience points in appropriate order.
#### 
Input

        It consists of 2 lines. The first line consists of a single integer N, the total number of men available to join the two forces. The next line comprises on N space separated integers, each integer denoting the experience points of a single man.

Ouput :

        Ouput 2 lines. The first line comprises of space separated integers denoting the experience points of every man in Bajirao's Force in the appropriate order. The next line comprises of space-separated integers denoting the experience points of every man in Baba's force in the appropriate order.

Constraints :

        1<=N<=1000
        1<=Experience Points<=10^9

Sample Input 

        7
        3 1 14 7 6 7 2

Sample Output

        2 6 14
        7 7 3 1

#### 16. Palindromic Numbers
Given A and B, count the numbers N such that A ≤ N ≤ B and N is a palindrome.

Examples:

        Palindromes: 121, 11 , 11411
        Not Palindromes: 122, 10

Input:

        First line contains T, the number of testcases. Each testcase consists of two integers A and B in one line.

Output:

        For each testcase, print the required answer in one line.

Constraints:

        1 ≤ T ≤ 10
        0 ≤ A ≤ B ≤ 105
Sample Input 

        2
        10 13
        20 30

Sample Output 

        1
        1

#### 28. A Needle in the Haystack
Our hacker, Little Stuart lately has been fascinated by ancient puzzles. One day going through some really old books he finds something scribbled on the corner of a page. Now Little Stuart believes that the scribbled text is more mysterious than it originally looks, so he decides to find every occurrence of all the permutations of the scribbled text in the entire book. Since this is a huge task, Little Stuart needs your help, he needs you to only figure out if any permutation of the scribbled text exists in the given text string, so he can save time and analyze only those text strings where a valid permutation is present.
#### 
Input:

        First line contains number of test cases T.Each test case contains two lines ,first line contains pattern and next line contains a text string. All characters in both the strings are in lowercase only [a-z].

Output:

        For each test case print "YES" or "NO" (quotes for clarity) depending on whether any permutation of the pattern exists in the text string.

Constraints:

        1 ≤ T ≤ 100
        1 ≤ |Pattern| ≤ 1000
        1 ≤ |Text String| ≤ 100000
Sample Input 

        3
        hack
        indiahacks
        code
        eddy
        coder
        iamredoc

Sample Output 

        YES
        NO
        YES









