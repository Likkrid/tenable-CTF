#!/usr/bin/env python3

from Crypto.Cipher import AES
import re

binary_pattern  = re.compile("password: (.*)\n")

terminal = """
Cracking turtles128.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 19199 bytes (19 KiB)

Extracting archive: turtles128.zip
--
Path = turtles128.zip
Type = zip
Physical Size = 19199

Everything is Ok

Size:       19051
Compressed: 19199
Cracking turtles127.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 19051 bytes (19 KiB)

Extracting archive: turtles127.zip
--
Path = turtles127.zip
Type = zip
Physical Size = 19051

Everything is Ok

Size:       18903
Compressed: 19051
Cracking turtles126.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18903 bytes (19 KiB)

Extracting archive: turtles126.zip
--
Path = turtles126.zip
Type = zip
Physical Size = 18903

Everything is Ok

Size:       18755
Compressed: 18903
Cracking turtles125.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18755 bytes (19 KiB)

Extracting archive: turtles125.zip
--
Path = turtles125.zip
Type = zip
Physical Size = 18755

Everything is Ok

Size:       18607
Compressed: 18755
Cracking turtles124.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18607 bytes (19 KiB)

Extracting archive: turtles124.zip
--
Path = turtles124.zip
Type = zip
Physical Size = 18607

Everything is Ok

Size:       18459
Compressed: 18607
Cracking turtles123.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18459 bytes (19 KiB)

Extracting archive: turtles123.zip
--
Path = turtles123.zip
Type = zip
Physical Size = 18459

Everything is Ok

Size:       18311
Compressed: 18459
Cracking turtles122.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18311 bytes (18 KiB)

Extracting archive: turtles122.zip
--
Path = turtles122.zip
Type = zip
Physical Size = 18311

Everything is Ok

Size:       18163
Compressed: 18311
Cracking turtles121.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18163 bytes (18 KiB)

Extracting archive: turtles121.zip
--
Path = turtles121.zip
Type = zip
Physical Size = 18163

Everything is Ok

Size:       18015
Compressed: 18163
Cracking turtles120.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 18015 bytes (18 KiB)

Extracting archive: turtles120.zip
--
Path = turtles120.zip
Type = zip
Physical Size = 18015

Everything is Ok

Size:       17867
Compressed: 18015
Cracking turtles119.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17867 bytes (18 KiB)

Extracting archive: turtles119.zip
--
Path = turtles119.zip
Type = zip
Physical Size = 17867

Everything is Ok

Size:       17719
Compressed: 17867
Cracking turtles118.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17719 bytes (18 KiB)

Extracting archive: turtles118.zip
--
Path = turtles118.zip
Type = zip
Physical Size = 17719

Everything is Ok

Size:       17571
Compressed: 17719
Cracking turtles117.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17571 bytes (18 KiB)

Extracting archive: turtles117.zip
--
Path = turtles117.zip
Type = zip
Physical Size = 17571

Everything is Ok

Size:       17430
Compressed: 17571
Cracking turtles116.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17430 bytes (18 KiB)

Extracting archive: turtles116.zip
--
Path = turtles116.zip
Type = zip
Physical Size = 17430

Everything is Ok

Size:       17295
Compressed: 17430
Cracking turtles115.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17295 bytes (17 KiB)

Extracting archive: turtles115.zip
--
Path = turtles115.zip
Type = zip
Physical Size = 17295

Everything is Ok

Size:       17166
Compressed: 17295
Cracking turtles114.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17166 bytes (17 KiB)

Extracting archive: turtles114.zip
--
Path = turtles114.zip
Type = zip
Physical Size = 17166

Everything is Ok

Size:       17045
Compressed: 17166
Cracking turtles113.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 17045 bytes (17 KiB)

Extracting archive: turtles113.zip
--
Path = turtles113.zip
Type = zip
Physical Size = 17045

Everything is Ok

Size:       16928
Compressed: 17045
Cracking turtles112.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16928 bytes (17 KiB)

Extracting archive: turtles112.zip
--
Path = turtles112.zip
Type = zip
Physical Size = 16928

Everything is Ok

Size:       16818
Compressed: 16928
Cracking turtles111.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16818 bytes (17 KiB)

Extracting archive: turtles111.zip
--
Path = turtles111.zip
Type = zip
Physical Size = 16818

Everything is Ok

Size:       16711
Compressed: 16818
Cracking turtles110.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16711 bytes (17 KiB)

Extracting archive: turtles110.zip
--
Path = turtles110.zip
Type = zip
Physical Size = 16711

Everything is Ok

Size:       16612
Compressed: 16711
Cracking turtles109.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16612 bytes (17 KiB)

Extracting archive: turtles109.zip
--
Path = turtles109.zip
Type = zip
Physical Size = 16612

Everything is Ok

Size:       16518
Compressed: 16612
Cracking turtles108.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16518 bytes (17 KiB)

Extracting archive: turtles108.zip
--
Path = turtles108.zip
Type = zip
Physical Size = 16518

Everything is Ok

Size:       16384
Compressed: 16518
Cracking turtles107.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16384 bytes (16 KiB)

Extracting archive: turtles107.zip
--
Path = turtles107.zip
Type = zip
Physical Size = 16384

Everything is Ok

Size:       16253
Compressed: 16384
Cracking turtles106.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16253 bytes (16 KiB)

Extracting archive: turtles106.zip
--
Path = turtles106.zip
Type = zip
Physical Size = 16253

Everything is Ok

Size:       16123
Compressed: 16253
Cracking turtles105.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 16123 bytes (16 KiB)

Extracting archive: turtles105.zip
--
Path = turtles105.zip
Type = zip
Physical Size = 16123

Everything is Ok

Size:       15992
Compressed: 16123
Cracking turtles104.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15992 bytes (16 KiB)

Extracting archive: turtles104.zip
--
Path = turtles104.zip
Type = zip
Physical Size = 15992

Everything is Ok

Size:       15862
Compressed: 15992
Cracking turtles103.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15862 bytes (16 KiB)

Extracting archive: turtles103.zip
--
Path = turtles103.zip
Type = zip
Physical Size = 15862

Everything is Ok

Size:       15732
Compressed: 15862
Cracking turtles102.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15732 bytes (16 KiB)

Extracting archive: turtles102.zip
--
Path = turtles102.zip
Type = zip
Physical Size = 15732

Everything is Ok

Size:       15597
Compressed: 15732
Cracking turtles101.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15597 bytes (16 KiB)

Extracting archive: turtles101.zip
--
Path = turtles101.zip
Type = zip
Physical Size = 15597

Everything is Ok

Size:       15464
Compressed: 15597
Cracking turtles100.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15464 bytes (16 KiB)

Extracting archive: turtles100.zip
--
Path = turtles100.zip
Type = zip
Physical Size = 15464

Everything is Ok

Size:       15329
Compressed: 15464
Cracking turtles99.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15329 bytes (15 KiB)

Extracting archive: turtles99.zip
--
Path = turtles99.zip
Type = zip
Physical Size = 15329

Everything is Ok

Size:       15198
Compressed: 15329
Cracking turtles98.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15198 bytes (15 KiB)

Extracting archive: turtles98.zip
--
Path = turtles98.zip
Type = zip
Physical Size = 15198

Everything is Ok

Size:       15069
Compressed: 15198
Cracking turtles97.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 15069 bytes (15 KiB)

Extracting archive: turtles97.zip
--
Path = turtles97.zip
Type = zip
Physical Size = 15069

Everything is Ok

Size:       14936
Compressed: 15069
Cracking turtles96.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14936 bytes (15 KiB)

Extracting archive: turtles96.zip
--
Path = turtles96.zip
Type = zip
Physical Size = 14936

Everything is Ok

Size:       14809
Compressed: 14936
Cracking turtles95.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14809 bytes (15 KiB)

Extracting archive: turtles95.zip
--
Path = turtles95.zip
Type = zip
Physical Size = 14809

Everything is Ok

Size:       14676
Compressed: 14809
Cracking turtles94.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14676 bytes (15 KiB)

Extracting archive: turtles94.zip
--
Path = turtles94.zip
Type = zip
Physical Size = 14676

Everything is Ok

Size:       14544
Compressed: 14676
Cracking turtles93.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14544 bytes (15 KiB)

Extracting archive: turtles93.zip
--
Path = turtles93.zip
Type = zip
Physical Size = 14544

Everything is Ok

Size:       14413
Compressed: 14544
Cracking turtles92.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14413 bytes (15 KiB)

Extracting archive: turtles92.zip
--
Path = turtles92.zip
Type = zip
Physical Size = 14413

Everything is Ok

Size:       14284
Compressed: 14413
Cracking turtles91.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14284 bytes (14 KiB)

Extracting archive: turtles91.zip
--
Path = turtles91.zip
Type = zip
Physical Size = 14284

Everything is Ok

Size:       14156
Compressed: 14284
Cracking turtles90.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14156 bytes (14 KiB)

Extracting archive: turtles90.zip
--
Path = turtles90.zip
Type = zip
Physical Size = 14156

Everything is Ok

Size:       14025
Compressed: 14156
Cracking turtles89.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 14025 bytes (14 KiB)

Extracting archive: turtles89.zip
--
Path = turtles89.zip
Type = zip
Physical Size = 14025

Everything is Ok

Size:       13894
Compressed: 14025
Cracking turtles88.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13894 bytes (14 KiB)

Extracting archive: turtles88.zip
--
Path = turtles88.zip
Type = zip
Physical Size = 13894

Everything is Ok

Size:       13766
Compressed: 13894
Cracking turtles87.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13766 bytes (14 KiB)

Extracting archive: turtles87.zip
--
Path = turtles87.zip
Type = zip
Physical Size = 13766

Everything is Ok

Size:       13634
Compressed: 13766
Cracking turtles86.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13634 bytes (14 KiB)

Extracting archive: turtles86.zip
--
Path = turtles86.zip
Type = zip
Physical Size = 13634

Everything is Ok

Size:       13507
Compressed: 13634
Cracking turtles85.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13507 bytes (14 KiB)

Extracting archive: turtles85.zip
--
Path = turtles85.zip
Type = zip
Physical Size = 13507

Everything is Ok

Size:       13375
Compressed: 13507
Cracking turtles84.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13375 bytes (14 KiB)

Extracting archive: turtles84.zip
--
Path = turtles84.zip
Type = zip
Physical Size = 13375

Everything is Ok

Size:       13245
Compressed: 13375
Cracking turtles83.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13245 bytes (13 KiB)

Extracting archive: turtles83.zip
--
Path = turtles83.zip
Type = zip
Physical Size = 13245

Everything is Ok

Size:       13118
Compressed: 13245
Cracking turtles82.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 13118 bytes (13 KiB)

Extracting archive: turtles82.zip
--
Path = turtles82.zip
Type = zip
Physical Size = 13118

Everything is Ok

Size:       12984
Compressed: 13118
Cracking turtles81.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12984 bytes (13 KiB)

Extracting archive: turtles81.zip
--
Path = turtles81.zip
Type = zip
Physical Size = 12984

Everything is Ok

Size:       12853
Compressed: 12984
Cracking turtles80.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12853 bytes (13 KiB)

Extracting archive: turtles80.zip
--
Path = turtles80.zip
Type = zip
Physical Size = 12853

Everything is Ok

Size:       12722
Compressed: 12853
Cracking turtles79.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12722 bytes (13 KiB)

Extracting archive: turtles79.zip
--
Path = turtles79.zip
Type = zip
Physical Size = 12722

Everything is Ok

Size:       12590
Compressed: 12722
Cracking turtles78.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12590 bytes (13 KiB)

Extracting archive: turtles78.zip
--
Path = turtles78.zip
Type = zip
Physical Size = 12590

Everything is Ok

Size:       12459
Compressed: 12590
Cracking turtles77.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12459 bytes (13 KiB)

Extracting archive: turtles77.zip
--
Path = turtles77.zip
Type = zip
Physical Size = 12459

Everything is Ok

Size:       12329
Compressed: 12459
Cracking turtles76.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12329 bytes (13 KiB)

Extracting archive: turtles76.zip
--
Path = turtles76.zip
Type = zip
Physical Size = 12329

Everything is Ok

Size:       12196
Compressed: 12329
Cracking turtles75.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12196 bytes (12 KiB)

Extracting archive: turtles75.zip
--
Path = turtles75.zip
Type = zip
Physical Size = 12196

Everything is Ok

Size:       12066
Compressed: 12196
Cracking turtles74.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 12066 bytes (12 KiB)

Extracting archive: turtles74.zip
--
Path = turtles74.zip
Type = zip
Physical Size = 12066

Everything is Ok

Size:       11935
Compressed: 12066
Cracking turtles73.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11935 bytes (12 KiB)

Extracting archive: turtles73.zip
--
Path = turtles73.zip
Type = zip
Physical Size = 11935

Everything is Ok

Size:       11807
Compressed: 11935
Cracking turtles72.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11807 bytes (12 KiB)

Extracting archive: turtles72.zip
--
Path = turtles72.zip
Type = zip
Physical Size = 11807

Everything is Ok

Size:       11676
Compressed: 11807
Cracking turtles71.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11676 bytes (12 KiB)

Extracting archive: turtles71.zip
--
Path = turtles71.zip
Type = zip
Physical Size = 11676

Everything is Ok

Size:       11545
Compressed: 11676
Cracking turtles70.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11545 bytes (12 KiB)

Extracting archive: turtles70.zip
--
Path = turtles70.zip
Type = zip
Physical Size = 11545

Everything is Ok

Size:       11410
Compressed: 11545
Cracking turtles69.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11410 bytes (12 KiB)

Extracting archive: turtles69.zip
--
Path = turtles69.zip
Type = zip
Physical Size = 11410

Everything is Ok

Size:       11279
Compressed: 11410
Cracking turtles68.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11279 bytes (12 KiB)

Extracting archive: turtles68.zip
--
Path = turtles68.zip
Type = zip
Physical Size = 11279

Everything is Ok

Size:       11143
Compressed: 11279
Cracking turtles67.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11143 bytes (11 KiB)

Extracting archive: turtles67.zip
--
Path = turtles67.zip
Type = zip
Physical Size = 11143

Everything is Ok

Size:       11009
Compressed: 11143
Cracking turtles66.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 11009 bytes (11 KiB)

Extracting archive: turtles66.zip
--
Path = turtles66.zip
Type = zip
Physical Size = 11009

Everything is Ok

Size:       10876
Compressed: 11009
Cracking turtles65.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10876 bytes (11 KiB)

Extracting archive: turtles65.zip
--
Path = turtles65.zip
Type = zip
Physical Size = 10876

Everything is Ok

Size:       10741
Compressed: 10876
Cracking turtles64.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10741 bytes (11 KiB)

Extracting archive: turtles64.zip
--
Path = turtles64.zip
Type = zip
Physical Size = 10741

Everything is Ok

Size:       10607
Compressed: 10741
Cracking turtles63.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10607 bytes (11 KiB)

Extracting archive: turtles63.zip
--
Path = turtles63.zip
Type = zip
Physical Size = 10607

Everything is Ok

Size:       10476
Compressed: 10607
Cracking turtles62.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10476 bytes (11 KiB)

Extracting archive: turtles62.zip
--
Path = turtles62.zip
Type = zip
Physical Size = 10476

Everything is Ok

Size:       10340
Compressed: 10476
Cracking turtles61.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10340 bytes (11 KiB)

Extracting archive: turtles61.zip
--
Path = turtles61.zip
Type = zip
Physical Size = 10340

Everything is Ok

Size:       10205
Compressed: 10340
Cracking turtles60.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10205 bytes (10 KiB)

Extracting archive: turtles60.zip
--
Path = turtles60.zip
Type = zip
Physical Size = 10205

Everything is Ok

Size:       10072
Compressed: 10205
Cracking turtles59.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 10072 bytes (10 KiB)

Extracting archive: turtles59.zip
--
Path = turtles59.zip
Type = zip
Physical Size = 10072

Everything is Ok

Size:       9943
Compressed: 10072
Cracking turtles58.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9943 bytes (10 KiB)

Extracting archive: turtles58.zip
--
Path = turtles58.zip
Type = zip
Physical Size = 9943

Everything is Ok

Size:       9812
Compressed: 9943
Cracking turtles57.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9812 bytes (10 KiB)

Extracting archive: turtles57.zip
--
Path = turtles57.zip
Type = zip
Physical Size = 9812

Everything is Ok

Size:       9681
Compressed: 9812
Cracking turtles56.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9681 bytes (10 KiB)

Extracting archive: turtles56.zip
--
Path = turtles56.zip
Type = zip
Physical Size = 9681

Everything is Ok

Size:       9548
Compressed: 9681
Cracking turtles55.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9548 bytes (10 KiB)

Extracting archive: turtles55.zip
--
Path = turtles55.zip
Type = zip
Physical Size = 9548

Everything is Ok

Size:       9416
Compressed: 9548
Cracking turtles54.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9416 bytes (10 KiB)

Extracting archive: turtles54.zip
--
Path = turtles54.zip
Type = zip
Physical Size = 9416

Everything is Ok

Size:       9286
Compressed: 9416
Cracking turtles53.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9286 bytes (10 KiB)

Extracting archive: turtles53.zip
--
Path = turtles53.zip
Type = zip
Physical Size = 9286

Everything is Ok

Size:       9155
Compressed: 9286
Cracking turtles52.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9155 bytes (9 KiB)

Extracting archive: turtles52.zip
--
Path = turtles52.zip
Type = zip
Physical Size = 9155

Everything is Ok

Size:       9024
Compressed: 9155
Cracking turtles51.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 9024 bytes (9 KiB)

Extracting archive: turtles51.zip
--
Path = turtles51.zip
Type = zip
Physical Size = 9024

Everything is Ok

Size:       8893
Compressed: 9024
Cracking turtles50.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8893 bytes (9 KiB)

Extracting archive: turtles50.zip
--
Path = turtles50.zip
Type = zip
Physical Size = 8893

Everything is Ok

Size:       8760
Compressed: 8893
Cracking turtles49.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8760 bytes (9 KiB)

Extracting archive: turtles49.zip
--
Path = turtles49.zip
Type = zip
Physical Size = 8760

Everything is Ok

Size:       8624
Compressed: 8760
Cracking turtles48.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8624 bytes (9 KiB)

Extracting archive: turtles48.zip
--
Path = turtles48.zip
Type = zip
Physical Size = 8624

Everything is Ok

Size:       8488
Compressed: 8624
Cracking turtles47.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8488 bytes (9 KiB)

Extracting archive: turtles47.zip
--
Path = turtles47.zip
Type = zip
Physical Size = 8488

Everything is Ok

Size:       8351
Compressed: 8488
Cracking turtles46.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8351 bytes (9 KiB)

Extracting archive: turtles46.zip
--
Path = turtles46.zip
Type = zip
Physical Size = 8351

Everything is Ok

Size:       8214
Compressed: 8351
Cracking turtles45.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8214 bytes (9 KiB)

Extracting archive: turtles45.zip
--
Path = turtles45.zip
Type = zip
Physical Size = 8214

Everything is Ok

Size:       8082
Compressed: 8214
Cracking turtles44.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 8082 bytes (8 KiB)

Extracting archive: turtles44.zip
--
Path = turtles44.zip
Type = zip
Physical Size = 8082

Everything is Ok

Size:       7948
Compressed: 8082
Cracking turtles43.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7948 bytes (8 KiB)

Extracting archive: turtles43.zip
--
Path = turtles43.zip
Type = zip
Physical Size = 7948

Everything is Ok

Size:       7814
Compressed: 7948
Cracking turtles42.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7814 bytes (8 KiB)

Extracting archive: turtles42.zip
--
Path = turtles42.zip
Type = zip
Physical Size = 7814

Everything is Ok

Size:       7681
Compressed: 7814
Cracking turtles41.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7681 bytes (8 KiB)

Extracting archive: turtles41.zip
--
Path = turtles41.zip
Type = zip
Physical Size = 7681

Everything is Ok

Size:       7544
Compressed: 7681
Cracking turtles40.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7544 bytes (8 KiB)

Extracting archive: turtles40.zip
--
Path = turtles40.zip
Type = zip
Physical Size = 7544

Everything is Ok

Size:       7409
Compressed: 7544
Cracking turtles39.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7409 bytes (8 KiB)

Extracting archive: turtles39.zip
--
Path = turtles39.zip
Type = zip
Physical Size = 7409

Everything is Ok

Size:       7273
Compressed: 7409
Cracking turtles38.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7273 bytes (8 KiB)

Extracting archive: turtles38.zip
--
Path = turtles38.zip
Type = zip
Physical Size = 7273

Everything is Ok

Size:       7139
Compressed: 7273
Cracking turtles37.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7139 bytes (7 KiB)

Extracting archive: turtles37.zip
--
Path = turtles37.zip
Type = zip
Physical Size = 7139

Everything is Ok

Size:       7008
Compressed: 7139
Cracking turtles36.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 7008 bytes (7 KiB)

Extracting archive: turtles36.zip
--
Path = turtles36.zip
Type = zip
Physical Size = 7008

Everything is Ok

Size:       6867
Compressed: 7008
Cracking turtles35.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6867 bytes (7 KiB)

Extracting archive: turtles35.zip
--
Path = turtles35.zip
Type = zip
Physical Size = 6867

Everything is Ok

Size:       6732
Compressed: 6867
Cracking turtles34.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6732 bytes (7 KiB)

Extracting archive: turtles34.zip
--
Path = turtles34.zip
Type = zip
Physical Size = 6732

Everything is Ok

Size:       6595
Compressed: 6732
Cracking turtles33.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6595 bytes (7 KiB)

Extracting archive: turtles33.zip
--
Path = turtles33.zip
Type = zip
Physical Size = 6595

Everything is Ok

Size:       6454
Compressed: 6595
Cracking turtles32.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6454 bytes (7 KiB)

Extracting archive: turtles32.zip
--
Path = turtles32.zip
Type = zip
Physical Size = 6454

Everything is Ok

Size:       6320
Compressed: 6454
Cracking turtles31.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6320 bytes (7 KiB)

Extracting archive: turtles31.zip
--
Path = turtles31.zip
Type = zip
Physical Size = 6320

Everything is Ok

Size:       6185
Compressed: 6320
Cracking turtles30.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6185 bytes (7 KiB)

Extracting archive: turtles30.zip
--
Path = turtles30.zip
Type = zip
Physical Size = 6185

Everything is Ok

Size:       6044
Compressed: 6185
Cracking turtles29.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 6044 bytes (6 KiB)

Extracting archive: turtles29.zip
--
Path = turtles29.zip
Type = zip
Physical Size = 6044

Everything is Ok

Size:       5907
Compressed: 6044
Cracking turtles28.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5907 bytes (6 KiB)

Extracting archive: turtles28.zip
--
Path = turtles28.zip
Type = zip
Physical Size = 5907

Everything is Ok

Size:       5771
Compressed: 5907
Cracking turtles27.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5771 bytes (6 KiB)

Extracting archive: turtles27.zip
--
Path = turtles27.zip
Type = zip
Physical Size = 5771

Everything is Ok

Size:       5634
Compressed: 5771
Cracking turtles26.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5634 bytes (6 KiB)

Extracting archive: turtles26.zip
--
Path = turtles26.zip
Type = zip
Physical Size = 5634

Everything is Ok

Size:       5496
Compressed: 5634
Cracking turtles25.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5496 bytes (6 KiB)

Extracting archive: turtles25.zip
--
Path = turtles25.zip
Type = zip
Physical Size = 5496

Everything is Ok

Size:       5357
Compressed: 5496
Cracking turtles24.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5357 bytes (6 KiB)

Extracting archive: turtles24.zip
--
Path = turtles24.zip
Type = zip
Physical Size = 5357

Everything is Ok

Size:       5218
Compressed: 5357
Cracking turtles23.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5218 bytes (6 KiB)

Extracting archive: turtles23.zip
--
Path = turtles23.zip
Type = zip
Physical Size = 5218

Everything is Ok

Size:       5080
Compressed: 5218
Cracking turtles22.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 5080 bytes (5 KiB)

Extracting archive: turtles22.zip
--
Path = turtles22.zip
Type = zip
Physical Size = 5080

Everything is Ok

Size:       4943
Compressed: 5080
Cracking turtles21.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4943 bytes (5 KiB)

Extracting archive: turtles21.zip
--
Path = turtles21.zip
Type = zip
Physical Size = 4943

Everything is Ok

Size:       4802
Compressed: 4943
Cracking turtles20.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4802 bytes (5 KiB)

Extracting archive: turtles20.zip
--
Path = turtles20.zip
Type = zip
Physical Size = 4802

Everything is Ok

Size:       4661
Compressed: 4802
Cracking turtles19.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4661 bytes (5 KiB)

Extracting archive: turtles19.zip
--
Path = turtles19.zip
Type = zip
Physical Size = 4661

Everything is Ok

Size:       4523
Compressed: 4661
Cracking turtles18.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4523 bytes (5 KiB)

Extracting archive: turtles18.zip
--
Path = turtles18.zip
Type = zip
Physical Size = 4523

Everything is Ok

Size:       4384
Compressed: 4523
Cracking turtles17.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4384 bytes (5 KiB)

Extracting archive: turtles17.zip
--
Path = turtles17.zip
Type = zip
Physical Size = 4384

Everything is Ok

Size:       4243
Compressed: 4384
Cracking turtles16.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4243 bytes (5 KiB)

Extracting archive: turtles16.zip
--
Path = turtles16.zip
Type = zip
Physical Size = 4243

Everything is Ok

Size:       4102
Compressed: 4243
Cracking turtles15.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 4102 bytes (5 KiB)

Extracting archive: turtles15.zip
--
Path = turtles15.zip
Type = zip
Physical Size = 4102

Everything is Ok

Size:       3961
Compressed: 4102
Cracking turtles14.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3961 bytes (4 KiB)

Extracting archive: turtles14.zip
--
Path = turtles14.zip
Type = zip
Physical Size = 3961

Everything is Ok

Size:       3820
Compressed: 3961
Cracking turtles13.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3820 bytes (4 KiB)

Extracting archive: turtles13.zip
--
Path = turtles13.zip
Type = zip
Physical Size = 3820

Everything is Ok

Size:       3687
Compressed: 3820
Cracking turtles12.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3687 bytes (4 KiB)

Extracting archive: turtles12.zip
--
Path = turtles12.zip
Type = zip
Physical Size = 3687

Everything is Ok

Size:       3546
Compressed: 3687
Cracking turtles11.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3546 bytes (4 KiB)

Extracting archive: turtles11.zip
--
Path = turtles11.zip
Type = zip
Physical Size = 3546

Everything is Ok

Size:       3408
Compressed: 3546
Cracking turtles10.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3408 bytes (4 KiB)

Extracting archive: turtles10.zip
--
Path = turtles10.zip
Type = zip
Physical Size = 3408

Everything is Ok

Size:       3269
Compressed: 3408
Cracking turtles9.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3269 bytes (4 KiB)

Extracting archive: turtles9.zip
--
Path = turtles9.zip
Type = zip
Physical Size = 3269

Everything is Ok

Size:       3130
Compressed: 3269
Cracking turtles8.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 3130 bytes (4 KiB)

Extracting archive: turtles8.zip
--
Path = turtles8.zip
Type = zip
Physical Size = 3130

Everything is Ok

Size:       2991
Compressed: 3130
Cracking turtles7.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2991 bytes (3 KiB)

Extracting archive: turtles7.zip
--
Path = turtles7.zip
Type = zip
Physical Size = 2991

Everything is Ok

Size:       2852
Compressed: 2991
Cracking turtles6.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2852 bytes (3 KiB)

Extracting archive: turtles6.zip
--
Path = turtles6.zip
Type = zip
Physical Size = 2852

Everything is Ok

Size:       2713
Compressed: 2852
Cracking turtles5.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2713 bytes (3 KiB)

Extracting archive: turtles5.zip
--
Path = turtles5.zip
Type = zip
Physical Size = 2713

Everything is Ok

Size:       2574
Compressed: 2713
Cracking turtles4.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2574 bytes (3 KiB)

Extracting archive: turtles4.zip
--
Path = turtles4.zip
Type = zip
Physical Size = 2574

Everything is Ok

Size:       2435
Compressed: 2574
Cracking turtles3.zip… Found password: 1

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2435 bytes (3 KiB)

Extracting archive: turtles3.zip
--
Path = turtles3.zip
Type = zip
Physical Size = 2435

Everything is Ok

Size:       2296
Compressed: 2435
Cracking turtles2.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2296 bytes (3 KiB)

Extracting archive: turtles2.zip
--
Path = turtles2.zip
Type = zip
Physical Size = 2296

Everything is Ok

Size:       2157
Compressed: 2296
Cracking turtles1.zip… Found password: 0

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2157 bytes (3 KiB)

Extracting archive: turtles1.zip
--
Path = turtles1.zip
Type = zip
Physical Size = 2157

Everything is Ok

Size:       2041

"""

binary = ''.join(binary_pattern.findall(terminal))
cipher = hex(int(binary,2))[2:]

key = bytes.fromhex("ed570e22d458e25734fc08d849961da9")
aes = AES.new(key, AES.MODE_ECB)
print(aes.decrypt(bytes.fromhex(cipher)).decode())
#flag{steg0_a3s}