# Linux 學習筆記

資工二 李易 111010512

## 第一週

### 系統安裝

先前往 [ftp.iij.ad.jp](http://ftp.iij.ad.jp/pub/linux/centos-vault/7.6.1810/isos/x86_64/)下載 [CentOS-7-x86_64-LiveKDE-1810.iso](http://ftp.iij.ad.jp/pub/linux/centos-vault/7.6.1810/isos/x86_64/CentOS-7-x86_64-LiveKDE-1810.iso)。
(備註：CentOS 從第 7 版開始就只支援 64 bits)

![](imgur/0N3XUp7.png)

下載完畢後，再前往 VirtualBox [官網](https://www.virtualbox.org/wiki/Downloads)取得最新版安裝包及擴展包。
(備註：也可以下載VMware。其中，VMware Play是免費版，VMware Workstation效能功能都比較好)

![](imgur/qATijbY.png)

安裝完畢後，點選介面內的新增按鈕，並進行以下配置：
(備註：擴展包只要直接點兩下就好，然後再到 `File > Tools > Extension Pack Manager` 進行查看)

![](imgur/ANvpw7P.png)

隨後啟動虛擬機，並點選 CentOS 桌面左下角的開始圖標，開始進行 Install。
(備註：在安裝過程中，管理員的密碼要設定成 `centos`，使用者的名稱、密碼要設定成 `user`)

![](imgur/obelyKn.png)

等到一切就緒後，再從 VirtualBox 那裏移除原本的光碟檔，然後重新登入，並確認是否設定成功。
(備註：重新登入時還要再設定License，直接勾選 Aceept 然後 Continue 就好)

### 相關比較

#### User vs Root

![](imgur/7ALYJs6.png)

#### Windows vs Linux

Windows: ipconfig
Linux: ifconfig

![](imgur/QMshcds.png)

#### VMware vs VirtualBox

VMware 和 VirtualBox 在 NAT 上會有所不同。
VMware: NAT VM can talk to host. Host can also talk to VM.
VirtualBox: NAT VM can talk to host. Host can not talk to VM.

![](imgur/IP6b0cm.png)

### 課程資源

https://www.bilibili.com/video/BV1U14y1G7UJ?p=1&vd_source=f74a220251f63c0d2381f8c51b2cbdee

https://www.bilibili.com/video/BV1Ug411k71N/?spm_id_from=333.999.0.0&vd_source=f74a220251f63c0d2381f8c51b2cbdee

https://hackmd.io/@jenny126/CentOS7/%2F2vZs_D8GRv29KdIQiiv95g

https://www.bilibili.com/video/BV1z54y1z7yN/?spm_id_from=333.337.search-card.all.click&vd_source=f74a220251f63c0d2381f8c51b2cbdee

https://www.books.com.tw/products/0010755095

### 就業機會

https://we.51job.com/pc/search?keyword=linux&searchType=2&sortType=0&metro=

## 第二週

### 設定 NAT

前往 CentOS 在 VirtualBox 底下的網路卡設定，在`介面卡1`啟動`NAT`網路卡，在`介面卡2`啟動`僅限主機介面卡`，並選擇`VirtualBox Host-Only Ethernet Adapter`。如果找不到該介面卡，就前往`檔案 > 工具 > Network Manager`自行新增，且新增時要勾選`DHCP Server`。

### 終端機

`$`是一般使用者的提示符號。
`#`是超級使用者的提示符號。
`~`符號代表家目錄。例如在 Windows 底下，使用者的家目錄為 `C:\Users\E321-21`。
`pwd`指令代表`print work directory`。
`cd`指令代表`change directory`。
`cd ~`指令可以回到家目錄。
`cd -`指令可以回到上一個路徑。
`clear`指令可以清除終端機畫面。
`kill -9 [pid]`指令可以清除背景程式。
`echo $?` 指令可以顯示上一段程式碼的執行結果是對是錯。
`sudo`指令可以在執行階段切換成管理者，執行完畢後再切換回來。
`ifconfig`指令相當於 Windows 底下的`ipconfig`。

如果顯示`ifconfig: command not found`的錯誤，就輸入`sudo yum install net-tools`來進行安裝。之所以使用`yum`是因為在 CentOS 底下沒有`apt`。

![](imgur/Heg55iw.png)

![](imgur/9UI0ETj.png)

### 關閉防火牆

1. 輸入 `su` 進入超級使用者。
2. 輸入 `sudo yum install gedit` 安裝 `gedit` 套件。
3. close selinux  (gedit /etc/selinux/config)
4. save -> close -> reboot
5. 輸入 `getenforce` 進行確認。
6. 輸入 `systemctl stop firewalld` 停止防火牆。
7. 輸入 `systemctl disable firewalld` 關閉防火牆。
8. 輸入 `systemctl status firewalld` 檢查防火牆。

![](imgur/n7sdeMg.png)

![](imgur/0d1VMMp.png)

![](imgur/fR1yYQw.png)

![](imgur/BpdRwoe.png)

### 遠端登入

1. 輸入 `sudo yum install openssh-server -y` 安裝套件。
2. 輸入 `systemctl start sshd` 啟動伺服器。
3. 輸入 `systemctl status sshd` 檢查伺服器。

![](imgur/qYTwR6q.png)

前往 https://www.putty.org/ 下載 PuTTY
前往 https://winscp.net/eng/download.php 下載 WinSCP

在 PuTTY 下輸入 CentOS 對外主機的 IP 位址，然後按 Open，即可在登入後進行指令操作。

![](imgur/PcCc1BU.png)

在 WinSCP 下輸入 CentOS 對外主機的 IP 位址，然後按登入，即可在登入後進行檔案傳輸。

![](imgur/JKGNTid.png)

### 網頁伺服器

1. 輸入 `sudo yum install httpd -y` 安裝套件。
2. 輸入 `systemctl start httpd` 啟動伺服器。
3. 輸入 `systemctl status httpd` 檢查伺服器。
4. 輸入 `cd /var/www/html` 前往資料夾。
5. 輸入 `echo "hi" > hi.htm` 寫入檔案。
6. 回到本機瀏覽器。
7. 輸入 `虛擬機 IP 位址 + 檔案名` 進行確認。

![](imgur/WdAXW7Z.png)

![](imgur/fNgXoJb.png)

![](imgur/L9AVpB4.png)

## 第三週

### 架設網站

IPv6

#### 設定網路卡

![](imgur/I29VhrY.png)

![](imgur/UgCvh0b.png)

#### 檢查防火牆

![](imgur/lfDykTn.png)

#### 啟動伺服器

![](imgur/QaC3kGQ.png)

![](imgur/sERCh6W.png)

### 架設機器人

OpenAI + LINE + Vercel = GPT AI Assistant

https://mrmad.com.tw/chatgpt-line-robot-creation-teaching
> ![](imgur/0lpDcgT.png)

### C語言

先用 gedit 進行編寫，然後再用 gcc 進行編譯。

![](imgur/HBXewhz.png)

## 第四週

### 建立快照

https://quietbo.com/2021/07/04/virtualbox-%E9%82%84%E5%8E%9F%E4%B9%8B%E5%89%8D%E7%9A%84%E5%82%99%E4%BB%BD%E8%88%87%E9%82%84%E5%8E%9F%E6%96%B9%E5%BC%8F-%E5%BF%AB%E7%85%A7-%E5%BF%85%E5%AD%B8/

> ![](imgur/0zxHot9.png)

### 安裝 Wget

```
yum install wget
```

![](imgur/JScEFfy.png)

### 安裝 Conda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
press q
enter yes
press enter
enter no
/home/user/miniconda3/bin/conda config --set auto_activate_base false
cd
gedit .bashrc
export PATH=$PATH:/home/user/miniconda3/bin
restart konsole
```

![](imgur/hRDMilE.png)

![](imgur/sSJb3mB.png)

![](imgur/ewCq728.png)

![](imgur/qq05KU6.png)

![](imgur/Ofgu9xk.png)

![](imgur/nEN95pk.png)

![](imgur/5bfIfln.png)

![](imgur/n2EoLM7.png)

![](imgur/CvdLhlj.png)

![](imgur/kxcnznX.png)

![](imgur/qk4liHA.png)

![](imgur/olRljQS.png)

### 建立環境

```
conda init
conda create -n py310 python=3.10
restart konsole
```

![](imgur/tPi5fq7.png)

![](imgur/wfVyWM6.png)

### 測試環境

```
conda activate py310
python
exit()
conda deactivate
```

![](imgur/rzLo1Tc.png)

![](imgur/MQNKh7X.png)

### 安裝 FFmpeg

https://sysadminxpert.com/install-ffmpeg-on-centos-7/

> ![](imgur/DPnngvK.png)

### 安裝 VLC

```
yum install vlc
```

### 安裝 Whisper

```
yum install git
conda activate py310
pip install git+https://github.com/openai/whisper.git
pip install pytube
```

### 下載程式

```
touch subtitle.py
gedit subtitle.py
copy from https://raw.githubusercontent.com/smallko/test-whisper/main/gen_sub.py
paste
```

### 執行程式

```
python subtitle.py
```

![](imgur/nn2Oboj.png)

### 播放影片

```
vlc
```

### 編輯字幕

```
gedit p4switch1.srt
```

## 第五週

### 基礎

Linux 管理者名稱: root
Windows 管理者名稱: administrator
Linux 裡面第一支被執行的應用程式 (process id = 1):
* old: init
* new: systemd

    > ![](imgur/9v3IrH6.png)

0.0.0.0: 任一界面的IP

### 快捷鍵

https://blog.csdn.net/qq_45083975/article/details/105274397

> ![](imgur/oeZNfx3.png)

### 常用指令

chmod (change mode) +x (excutable)

> ![](imgur/sBf2BXL.png)

dmesg | more

> ![](imgur/waQuSmx.png)

clear

> 清除螢幕畫面

netstat

> ![](imgur/GJblAB1.png)

uname

> ![](imgur/r91rKsI.png)

hostnamectl

> ![](imgur/FCkrSxK.png)

PS1

> ![](imgur/AAcDHcF.png)

echo pts

> ![](imgur/GXo0Vy9.png)

fg

> ![](imgur/jF6i8DK.png)

ls

> ![](imgur/nRbEH7T.png)

### 更新密碼

https://www.unixmen.com/reset-root-password-centos-7/

> ![](imgur/7lCDO23.png)

## 第六週

### 4-1

/lib

> 動態函式庫: `lib` 開頭, `.so.*` 結尾
> 靜態函式庫: `lib` 開頭, `.a` 結尾

/mnt

> ![](imgur/7orlnRH.jpg)

### 4-2

ls

> ![](imgur/6RTWN0i.png)

> ![](imgur/XX1WcrJ.png)

> ![](imgur/hd4T29p.png)

特殊目錄

> ![](imgur/o6kdCQd.png)

cd

> ![](imgur/WwW2rHJ.png)

touch

> ![](imgur/58uuxRF.jpg)

> ![](imgur/4XpgE6V.png)

cat

> ![](imgur/d2pphXl.png)

pipe

> ![](imgur/mwYtS2y.png)

## 第八週

![](imgur/QnmvLQ2.png)

windows下"捷徑"可以連結到任意的"檔案"或者是"資料夾"

![](imgur/CgPUkQl.png)

![](imgur/l6ir7iV.png)

![](imgur/K9ba1lG.png)


https://dywang.csie.cyut.edu.tw/dywang/linuxsecurity/node39.html

![](imgur/aoBZhyN.png)

s = SUID
t = SBIT

r: 4
w: 3
x: 1

![](imgur/iRFj9DH.png)

典型的例子如 /tmp 的權限是 『drwxrwxrwt』，任何用戶都可在 /tmp 內新增、修改檔案，但僅有該檔案/目錄建立者與 root 能夠刪除自己的目錄或檔案。  (Sticky bit的功用)

![](imgur/04dFpZG.png)

切換身分

![](imgur/P6K25Ji.png)

![](imgur/uX4GEDU.png)

https://blog.51cto.com/u_13662393/2094920
> change time : 除了內容改變會變動外,屬性變動也會變更時間

![](imgur/XdIZsbn.png)

可以用 ntpdate 調整時區

![](imgur/PxEZuQp.png)

slink 符號連結

![](imgur/sqkad35.png)

hlink 硬連結

![](imgur/txbI0Ph.png)

修改環境變數

![](imgur/1KuBToJ.png)

dd

![](imgur/FmuhRwS.png)

顯示硬碟空間使用率

![](imgur/KCEN5DK.png)

## 第九週

du vs df

![](imgur/cX4r8W1.png)

du

![](imgur/19NPu9a.png)

sum

![](imgur/UIbWE0Q.png)

depth

![](imgur/rdm2P0b.png)

stdout

![](imgur/vFNc4Ga.png)

stderr

![](imgur/QGa5nzx.png)

![](imgur/ONXgvUc.png)

![](imgur/hwfWdnO.png)

![](imgur/n2Bpssn.png)

![](imgur/TyJhJtc.png)

hide

![](imgur/33f4zI5.png)

![](imgur/t3hchAF.png)

pipe

![](imgur/XkM2vfL.png)

xargs

![](imgur/u0nBuSg.png)

有名管道

![](imgur/b78OdI9.png)

![](imgur/IB7YxS2.png)

`>` `>>`

![](imgur/teKocib.png)

updatedb, locate

![](imgur/6LNDTnN.png)

![](imgur/LDOexlL.png)

find

![](imgur/vjJQaZW.png)

![](imgur/evBE5sK.png)

![](imgur/5eqxFiA.png)

期末必考:
https://blog.gtwang.org/linux/unix-linux-find-command-examples/

增量備份

![](imgur/Gnpr3ed.png)

![](imgur/FGVEfQU.png)
