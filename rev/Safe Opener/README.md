# Safe Opener
### Description
> Can you open this safe? I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

### Solution
Then you download the file from Description, you can get `"SafeOpener.java"`.
You compile the file by using `javac` command and generate `SafeOpener.class`.
Then you execute `SafeOpener.class`, you find that to input password is required.
From Description, because flag format is `picoCTF{password}`, you can get flag by getting correct password.
```
$ java SafeOpener
Enter password for the safe: aaa
YWFh
Password is incorrect

You have  2 attempt(s) left
Enter password for the safe: bbb
YmJi
Password is incorrect

You have  1 attempt(s) left
Enter password for the safe: ccc
Y2Nj
Password is incorrect

You have  0 attempt(s) left
```

Then you look source code of `SafeOpener.java`, you can find that the program encode inputted string by base64 and compare encoded string and `encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"`.
```java
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;


        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);

            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }

    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";

        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}
```

From this process, correct password is string that is decoded of `encodedKey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"` by base64.
String that is decoded of `encodedKey` by base64 is `pl3as3_l3t_m3_1nt0_th3_saf3`.
```
$ echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
pl3as3_l3t_m3_1nt0_th3_saf3
```

You can find that the password is correct by executing `SafeOpener.class` and inputting the password.
```
$ java SafeOpener
Enter password for the safe: pl3as3_l3t_m3_1nt0_th3_saf3
cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
Sesame open
```

Therefore, flag is `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`.