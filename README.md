# MonetDB-spec

openSUSE MonetDB RPM spec

[MonetDB](https://www.monetdb.org/Home) is an open source column-oriented
database management system developed at the Centrum
Wiskunde & Informatica (CWI) in the Netherlands.

It was designed to provide high performance on complex queries against large
databases, such as combining tables with hundreds of columns and millions of
rows.

這個 openSUSE MonetDB RPM spec 修改自 MonetDB Redhat RPM spec，
只是被我 disable 一些相關的功能，只留下我自己需要的部份。

同時也符合 openSUSE 的套件命名方式：  
bzip2-devel -> libbz2-devel  
shadow-utils -> pwdutils

注意： 
Oct2020 我發現 ODBC driver 使用之前的程式測試，
無法正確執行，所以目前 MonetDB ODBC driver 推測無法正確運作。
Oct2020-SP1 已修正 ODBC driver 問題。

