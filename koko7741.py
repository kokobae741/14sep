ó
Ê{]c           @   sK  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e j   Z e  j	 e  j
 d k r{ d n d  d   Z d   Z d   Z d d d	  Z d
 d d  Z d e f d     YZ d e j f d     YZ d Z e d GHe d j d d d d d d d d d g	   GHd   Z e d k rGe   n  d S(   iÿÿÿÿNt   ntt   clst   clearc         C   s    t  j j t  j j t   |  S(   N(   t   ost   patht   dirnamet   abspatht   __file__(   t	   file_name(    (    s   /sdcard/dcim/koko7741.pyt	   real_path   s    c         C   sn   xN t  t |    D]: } |  | j   |  | <|  | j d  r d |  | <q q Wg  |  D] } | rX | ^ qX S(   Nt   #t    (   t   ranget   lent   stript
   startswith(   t   arrayt   it   x(    (    s   /sdcard/dcim/koko7741.pyt   filter_array   s
    c         C   sd   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x- | D]% } |  j  d j |  | |  }  q7 W|  S(   Ns   [31;1mt   R1s   [31;2mt   R2s   [32;1mt   G1s   [33;1mt   Y1s   [35;1mt   P1s   [0mt   CCs   [{}](   t   replacet   format(   t   valuet   patternst   code(    (    s   /sdcard/dcim/koko7741.pyt   colors   s    #R   c      
   C   sR   t  d j d t j j   j d  d |  d | d |   }  t 
 |  GHWd  QXd  S(   NsI   {color}[{time}] [CC]Mencari Server {color}{status} [CC]{color}{value}[CC]t   times   %H:%MR   t   colort   status(   R   R   t   datetimet   nowt   strftimet   lock(   R   R"   R!   (    (    s   /sdcard/dcim/koko7741.pyt   log"   s     t   Injectc         C   sI   t  d j | | |    }  t " t j j |   t j j   Wd  QXd  S(   Ns   {}{} ({})        [CC](   R   R   R&   t   syst   stdoutt   writet   flush(   R   R"   R!   (    (    s   /sdcard/dcim/koko7741.pyt   log_replace+   s    t   injectc           B   s&   e  Z d    Z d d  Z d   Z RS(   c         C   s5   t  t |   j   t |  |  _ t |  |  _ d  S(   N(   t   superR.   t   __init__t   strt   inject_hostt   intt   inject_port(   t   selfR2   R4   (    (    s   /sdcard/dcim/koko7741.pyR0   2   s    s   [G1]c         C   s   t  | d | d  S(   NR!   (   R'   (   R5   R   R!   (    (    s   /sdcard/dcim/koko7741.pyR'   8   s    c         C   s,  yí t  j  t  j t  j  } | j |  j |  j f  | j d  t t d   j	   } t
 |  } t |  d k r |  j d d d d  S|  j d j |  j |  j   x< t rë | j   \ } } | j d  t | |  j   q° WWn8 t k
 r'} |  j d	 j |  j |  j  d d
 n Xd  S(   Ni   s   /config.txt.enci    s7   Frontend Domains not found. Please check config.txt.encR!   R   s    #====AJa Klalen Maca Donga====#
Local Host : 127.0.0.1
Local Port : 7741
Alhamdulillah Ebat Ya Wa (200 OK) 
Aja Ndrenges Bae Gah Wa !!!i   s!   Gagal!!!Mohon Restar Android andas   [R1](   t   sockett   AF_INETt   SOCK_STREAMt   bindR2   R4   t   listent   openR	   t	   readlinesR   R   R'   R   t   Truet   acceptt   recvt   domain_frontingt   startt	   Exception(   R5   t   socket_servert   frontend_domainst   socket_clientt   _t	   exception(    (    s   /sdcard/dcim/koko7741.pyRA   ;   s     	(   t   __name__t
   __module__R0   R'   RA   (    (    (    s   /sdcard/dcim/koko7741.pyR.   1   s   	R@   c           B   s2   e  Z d    Z d d d  Z d   Z d   Z RS(   c         C   sV   t  t |   j   | |  _ t j t j t j  |  _ | |  _ d |  _	 t
 |  _ d  S(   Ni   (   R/   R@   R0   RD   R6   R7   R8   t   socket_tunnelRE   t   buffer_sizeR=   t   daemon(   R5   RE   RD   (    (    s   /sdcard/dcim/koko7741.pyR0   N   s    			t	   DitemukanR   c         C   s   t  | d | d | d  S(   NR"   R!   (   R'   (   R5   R   R"   R!   (    (    s   /sdcard/dcim/koko7741.pyR'   W   s    c         C   sè   | | g } d } xÏ t  rã | d 7} t j | g  | d  \ } } } | rP Pn  | rÐ xw | D]l }	 y[ |	 j |  }
 |
 s Pn8 |	 | k r | j |
  n |	 | k r· | j |
  n  d } Wq] Pq] Xq] Wn  | d k r Pq q Wd  S(   Ni    i   i   i<   (   R=   t   selectR?   t   sendall(   R5   RJ   RE   RK   t   socketst   timeoutt	   socket_ioRF   t   errorst   sockt   data(    (    s   /sdcard/dcim/koko7741.pyt   handler[   s,    	
!  
  c         C   sv  yt  j |  j  j d  |  _ |  j d |  _ t |  j  d k r` |  j d r` |  j d n d |  _ |  j d j	 |  j |  j   |  j
 j t |  j  t |  j  f  |  j j d  |  j |  j
 |  j |  j  |  j j   |  j
 j   |  j d j	 |  j |  j  d	 d
 WnS t k
 rB|  j d d	 d n0 t k
 rq|  j d j	 |  j  d	 d n Xd  S(   Nt   :i    i   i   t   443s!   [CC]Kodipit Wa Delat Maning...!!!s   HTTP/1.1 200 OK

s   sukses 200 ok!!!R!   s   [G1]s   Connection errors   [CC]s   {} not responding(   t   randomt   choiceRD   t   splitt   proxy_host_portt
   proxy_hostR   t
   proxy_portR'   R   RJ   t   connectR1   R3   RE   RO   RV   RK   t   closet   OSErrort   TimeoutError(   R5   (    (    s   /sdcard/dcim/koko7741.pyt   runp   s    8()(   RH   RI   R0   R'   RV   Rc   (    (    (    s   /sdcard/dcim/koko7741.pyR@   M   s
   			s   [1;33ms*   (TULUNG GAH WA DI NGGO SING BENER YA WA) 
s   
s%   [G1][!]DUDU KULA :ORA KUAT TUKU KUOTAs)   [CC][G1][!]DUDU KULA :ORA KUAT TUKU PULSAsC   [CC][G1][!]KULA LAN BATUR SADAYA :TERUS LURU ELMU SAMPE TEKANG TUA sV   [CC][G1][!]WIS GAH WA NGECAPRAK BAE, AREP LURU SEGA, NGELI MANGAN NTAS NGOJEG BECA WA s.   [CC]==========================================s>   [CC][R1]>>>>>|[!]SET TEN POPON E 127.0.0.1 PORT 7741[!]|<<<<<<s'   [CC]Inject [!] TELEKAMPRETOS 2 in 1 [!]s   [CC]c          C   sP   d }  d } t  d  } | | k r4 t j d  n  d GHt d d  j   d  S(   Ns1    [G1][!] Ketik ken password E Wa, Ngarti Ora Son!t   b4nkma2ts    [!] input password [!] : s4    [!] password salah, sakola Beli Wa Pekara Kih! [!]
s$    [!] Nah Leres Wa Lanjuuuuuuuut [!]
s	   127.0.0.1t   7741(   t	   raw_inputR)   t   exitR.   RA   (   t   DRd   t
   user_input(    (    s   /sdcard/dcim/koko7741.pyt   main   s    t   __main__(   R   R)   RY   R6   RN   R#   t	   threadingt   RLockR&   t   systemt   nameR	   R   R   R'   R-   t   objectR.   t   ThreadR@   t   Gt   joinRj   RH   (    (    (    s   /sdcard/dcim/koko7741.pyt   <module>   s6    "				4				