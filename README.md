A simplified cache-based side-channel attack. With the aim to break a 6 bit encryption mechanism running on the "target VM".

My objective is to: Simulate a scenario where a VM attacker tries to guess bits of a target VM secret key using variations in cache access times.

The Python program will take 2 arguments

A CSV file with the following information:

Encryption Bit,Delay
0,0.1
1,0.2
2,0.3
3,0.4
4,0.5
5,0.6

Where the first column will represent the specific bit, and the second column the delay in seconds to be added.  The time will simulate a "cache delay" when using that specific key bit.
And a time delay that will represent the "cache latency" of an unknown key.


From my understanding:
The program will only use 6-bit keys. That means that a key will need to have a value between 0 and 63.  I a key of ' 1'  is passed, it means bit 0 is enabled for that key and the time delay for that bit must be added.  If a key of '32' is passed, it means bit 5 is enabled so a time delay of 0.6 must be added.

Using the bit delay file my program will perform a probePhase() where it will pass known keys to an encryption(str, key) method.  This encryption method will add proper delays depending on the bits used on the key.  The key can only be 6 bits long.  During this probe phase the program will store relevant information on the different keys passed and the "cache latency" that is incurred after using these keys.
Using these cache profile the program will output the set of key(s) that are in the +/- 0.05 seconds ballpark of the cache latency passed as input.
