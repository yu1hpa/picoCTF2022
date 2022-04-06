# Fresh Java
### Description
> Can you get the flag? Reverse engineer this Java program.

### Solution
Then you download the file from Description, you can get `"KeygenMe.class"`.
Then you execute the file, you find that to input key is required.
So, you can infer that you can get flag by getting correct key.
```
$ java KeygenMe
Enter key:
aaaa
Invalid key
```

Then you do reverse compile of `KeygenMe.class` by using `jd-gui`, you can get follow source code.
```java
import java.util.Scanner;

public class KeygenMe {
  public static void main(String[] paramArrayOfString) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter key:");
    String str = scanner.nextLine();
    if (str.length() != 34) {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(33) != '}') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(32) != '7') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(31) != '9') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(30) != '9') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(29) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(28) != '2') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(27) != 'e') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(26) != '4') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(25) != '8') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(24) != '_') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(23) != 'd') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(22) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(21) != 'r') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(20) != '1') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(19) != 'u') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(18) != 'q') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(17) != '3') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(16) != 'r') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(15) != '_') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(14) != 'g') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(13) != 'n') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(12) != '1') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(11) != 'l') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(10) != '0') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(9) != '0') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(8) != '7') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(7) != '{') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(6) != 'F') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(5) != 'T') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(4) != 'C') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(3) != 'o') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(2) != 'c') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(1) != 'i') {
      System.out.println("Invalid key");
      return;
    } 
    if (str.charAt(0) != 'p') {
      System.out.println("Invalid key");
      return;
    } 
    System.out.println("Valid key");
  }
}
```

According to the source code, the program extract a character of inputted key and correct key one by one and compare these caracters.
Then you look characters compared with character of inputted key, the string is `picoCTF{700l1ng_r3qu1r3d_84e23997}`. It is correct key.
If you extract `KeygenMe.class` and input above key, you can find the key is correct.
```
$ java KeygenMe
Enter key:
picoCTF{700l1ng_r3qu1r3d_84e23997}
Valid key
```

Therefore, flag is `picoCTF{700l1ng_r3qu1r3d_84e23997}`.

### Writer
Yajirushi