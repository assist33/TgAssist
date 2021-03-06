U
    N�_�  �                   @   sx  d dl Z d dlmZmZmZ d dlmZ d dlmZ d dlmZm	Z	 d dl
mZ d dlZd dlZd dlZd dlmZ d dlZd dlZdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Zdd� Ze�d� e�  e�� Ze�d� ed d ZdZeek�r�e d�Z!e d�Z"e�d� e�de! d � e�d e" d � e#ej$d! ej% d" ej$ d# ej% d$ � e#ej$d! ej% d% ej$ d# ej% d& � e�&d'� e�'�  e�d� e�  e �(d(�Z)ed d) Z*e+ed d �Z,ed*e*e,�Z-d+Z.d,Z/e-�0ej1e.d-��d.d/� �Z2e-�3�  e+e-�4� �5� �Z6e)�7e/e6� e#ej$d! ej% d0 ej$ d# ej% d1 � e#ej$d! ej% d2 ej$ d# ej% d3 � e#ej$d! ej% d4 ej$ d# ej% d5 � e#ej$d! ej% d6 ej$ d# ej% d7 � e#ej$d! ej% d8 ej$ d# ej% d9 � e d:�Z8e8d0k�re�  e8d2k�r,e�  e8d4k�r<e�  e8d6k�rLe�  e8d8k�r\e�  e8d;k�rle9�  e-�:�  dS )<�    N)�TelegramClient�sync�events)�JoinChannelRequest)�InviteToChannelRequest)�	functions�types)�UserNotMutualContactError)�Forec                  C   s�  d} d}t tj| d  � t tj| d  � t tj| d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d	  tj | d  � t tj| d  tj |d	  tj | d  � t tj| d  tj |d	  tj | d  � t tj| d  tj |d	  tj | d  � t tj| d  tj |d  tj | d  tj |d
  tj | d  tj |d  tj | d  � t tj| d  tj |d
  tj | d  tj |d  tj | d  tj |d
  tj | d  � t tj| d  tj |d
  tj | d  tj |d  tj | d  tj |d
  tj | d  � t tj| d  tj |d
  tj | d  tj |d  tj | d  tj |d
  tj | d  � t tj| d  tj |d  tj | d
  tj |d  tj | d  � t tj| d  tj |d
  tj | d  tj |d  tj | d  tj |d
  tj | d  tj |d  tj | d  tj |d
  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d  tj | d  tj |d  tj | d  � t tj| d  tj |d  tj | d  tj |d  tj | d  tj |d
  tj | d  tj |d  tj | d  tj |d  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  tj |d  tj | d  � t tj| d  � t tj| d  � d}t tj|d  � t tjd � t tj|d  � d S )N�   °�   ©�(   �
   �   �   �   �   �   �   �   �   �   �   �_z
TelegramAssist version 1.0)�printr
   �RED�GREEN)�r�gZram� r   �'/storage/emulated/0/bot/newbot/test2.py�logo   s<    .......ffffJ�.J�...r!   c                  C   s,   t d�} t d�}t�| |� t�d� qd S )Nu   введите ник:u"   введите сообщение:r   )�input�client�send_message�time�sleep)Znik�mr   r   r    �spam,   s    r(   c                  C   s�   t d�} t d�}t| d�}|D ]f}t|�}|dkrt|�}t�||� ttjd tj	 d tj d tj	 d | d	 � t
�d
� qd S )Nu*   введите название базы: �#   введите сообщение: r   �   �[�+�]u-    сообщение пользователю u    отправлено :)�   )r"   �open�len�strr#   r$   r   r
   r   r   r%   r&   )�baza�mess�f�liner   �usr   r   r    �spam22   s    
4r7   c                  C   s�   t d�} | d }t|d�}|��  t�| �D ]8}t|d�}t|j�}t�dd|�}|�	d| d � q,t
tjd	 tj d
 tj d tj d |  d � |��  t��  d S )Nu   введите чат: z.txt�w�a�None� �@�
r+   r,   r-   u    база username чата u    создана)r"   r/   �closer#   �iter_participantsr1   �username�re�sub�writer   r
   r   r   �sys�exit)�chatZname1r4   �user�pr@   �namer   r   r    �parser>   s    


4rJ   c                 C   s2  t d�}t| d�}|D �]}t|�}|dkrztt|�� W n6   ttjd � ttjd � t�	d� Y qY nX ttjd tj
 d tj d	 tj
 | � t�	d
� zt�||� W n6   ttjd � ttjd � t�	d� Y qY nX ttjd tj
 d tj d	 tj
 d | � t�	d
� qd S )Nr)   r   �   u<   eror не возможно добавиться в чат :(u   таймаут 2 минуты�x   r+   r,   r-   r.   uA   eror не возможно написать сообщение :(u   таймаут 3сr*   z send message )r"   r/   r0   r#   r   r   r
   r   r%   r&   r   r$   )r2   r3   r4   rF   Zpror   r   r    �piarL   s.    



,


0rM   c                  C   s�   t tjd tj d tj d tj d � t tjd tj d tj d tj d � td�} | dkrxtd�}t|� | dkr�d	}t|� d S )
Nr+   �1r-   u    своя база�2z	 default �>>>u   название базы: z	baza2.txt)r   r
   r   r   r"   rM   )�numbr2   r   r   r    �piarspame   s    ,,rR   c                  C   s�   t d�} t d�}t�| �D ]�}t|j�}t�dd|�}t|�}|dkr�d| }zttj	j
||gd�� W n"   ttjd | � Y qY nX ttjd	 tj d
 tj d tj d | � t�d� qt��  t��  d S )NuM    чат из которого добавляем пользователей: u@    чат куда добавляем пользователей: r:   r;   r*   r<   )ZchannelZuserszeror r+   r,   r-   z DONE r   )r"   r#   r?   r1   r@   rA   rB   r0   r   Zchannelsr   r   r
   r   r   r%   r&   r4   r>   rD   rE   )Zchat1Zchat2rG   r6   Zusrr   Zusr1r   r   r    �invitep   s(    
�
0rS   �clearz
config.iniZtelegram�api_hash�0zapi_id: z
api_hash: zecho "[telegram]" > config.inizecho "api_id =z " >> config.inizecho "api_hash =r+   r,   r-   z DONE�!u+    перезапустите скрипт :)r*   z.1323938876:AAEy8k9ng0FA5uI3j5rXWpEeIxtSj_08xNs�api_idZsessioni(� i���L)Zchatsc                 �   s$   | j �� d }t�t|�I d H  d S )N�message)rY   Zto_dict�botr$   �chat_id)Zeventr3   r   r   r    �normal_handler�   s    r\   rN   z	 tgspamerrO   z parser �3u`    piarspam(спамит по каналам из базы работает не стабилно)�4z invite to chat�5u    userspam(по базам)rP   �6);ZtelebotZtelethonr   r   r   Ztelethon.tl.functions.channelsr   r   r   r   Ztelethon.errorsr	   �osZconfigparserr%   Zcoloramar
   rD   rA   r!   r(   r7   rJ   rM   rR   rS   �systemZConfigParserZconfig�read�hashr   r"   ZaidZahashr   r   r   r&   rE   ZTeleBotrZ   rX   r1   rU   r#   rF   r[   ZonZ
NewMessager\   �startZget_meZ	stringify�infor$   rQ   �deleteZrun_until_disconnectedr   r   r   r    �<module>   s�   



,,



,,,,,





