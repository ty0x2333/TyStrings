FasdUAS 1.101.10   ��   ��    k             l     ��  ��      tystrings.scpt     � 	 	    t y s t r i n g s . s c p t   
  
 l     ��������  ��  ��        l     ��  ��      The MIT License (MIT)     �   ,   T h e   M I T   L i c e n s e   ( M I T )      l     ��  ��           �           l     ��  ��    ( " Copyright (c) 2017 luckytianyiyan     �   D   C o p y r i g h t   ( c )   2 0 1 7   l u c k y t i a n y i y a n      l     ��  ��           �          !   l     �� " #��   " S M Permission is hereby granted, free of charge, to any person obtaining a copy    # � $ $ �   P e r m i s s i o n   i s   h e r e b y   g r a n t e d ,   f r e e   o f   c h a r g e ,   t o   a n y   p e r s o n   o b t a i n i n g   a   c o p y !  % & % l     �� ' (��   ' T N of this software and associated documentation files (the "Software"), to deal    ( � ) ) �   o f   t h i s   s o f t w a r e   a n d   a s s o c i a t e d   d o c u m e n t a t i o n   f i l e s   ( t h e   " S o f t w a r e " ) ,   t o   d e a l &  * + * l     �� , -��   , S M in the Software without restriction, including without limitation the rights    - � . . �   i n   t h e   S o f t w a r e   w i t h o u t   r e s t r i c t i o n ,   i n c l u d i n g   w i t h o u t   l i m i t a t i o n   t h e   r i g h t s +  / 0 / l     �� 1 2��   1 P J to use, copy, modify, merge, publish, distribute, sublicense, and/or sell    2 � 3 3 �   t o   u s e ,   c o p y ,   m o d i f y ,   m e r g e ,   p u b l i s h ,   d i s t r i b u t e ,   s u b l i c e n s e ,   a n d / o r   s e l l 0  4 5 4 l     �� 6 7��   6 L F copies of the Software, and to permit persons to whom the Software is    7 � 8 8 �   c o p i e s   o f   t h e   S o f t w a r e ,   a n d   t o   p e r m i t   p e r s o n s   t o   w h o m   t h e   S o f t w a r e   i s 5  9 : 9 l     �� ; <��   ; ? 9 furnished to do so, subject to the following conditions:    < � = = r   f u r n i s h e d   t o   d o   s o ,   s u b j e c t   t o   t h e   f o l l o w i n g   c o n d i t i o n s : :  > ? > l     �� @ A��   @       A � B B    ?  C D C l     �� E F��   E U O The above copyright notice and this permission notice shall be included in all    F � G G �   T h e   a b o v e   c o p y r i g h t   n o t i c e   a n d   t h i s   p e r m i s s i o n   n o t i c e   s h a l l   b e   i n c l u d e d   i n   a l l D  H I H l     �� J K��   J 6 0 copies or substantial portions of the Software.    K � L L `   c o p i e s   o r   s u b s t a n t i a l   p o r t i o n s   o f   t h e   S o f t w a r e . I  M N M l     �� O P��   O       P � Q Q    N  R S R l     �� T U��   T Q K THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    U � V V �   T H E   S O F T W A R E   I S   P R O V I D E D   " A S   I S " ,   W I T H O U T   W A R R A N T Y   O F   A N Y   K I N D ,   E X P R E S S   O R S  W X W l     �� Y Z��   Y O I IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    Z � [ [ �   I M P L I E D ,   I N C L U D I N G   B U T   N O T   L I M I T E D   T O   T H E   W A R R A N T I E S   O F   M E R C H A N T A B I L I T Y , X  \ ] \ l     �� ^ _��   ^ R L FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    _ � ` ` �   F I T N E S S   F O R   A   P A R T I C U L A R   P U R P O S E   A N D   N O N I N F R I N G E M E N T .   I N   N O   E V E N T   S H A L L   T H E ]  a b a l     �� c d��   c M G AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER    d � e e �   A U T H O R S   O R   C O P Y R I G H T   H O L D E R S   B E   L I A B L E   F O R   A N Y   C L A I M ,   D A M A G E S   O R   O T H E R b  f g f l     �� h i��   h T N LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,    i � j j �   L I A B I L I T Y ,   W H E T H E R   I N   A N   A C T I O N   O F   C O N T R A C T ,   T O R T   O R   O T H E R W I S E ,   A R I S I N G   F R O M , g  k l k l     �� m n��   m T N OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    n � o o �   O U T   O F   O R   I N   C O N N E C T I O N   W I T H   T H E   S O F T W A R E   O R   T H E   U S E   O R   O T H E R   D E A L I N G S   I N   T H E l  p q p l     �� r s��   r  
 SOFTWARE.    s � t t    S O F T W A R E . q  u v u l     ��������  ��  ��   v  w x w l     ��������  ��  ��   x  y z y l    	 {���� { r     	 | } | c      ~  ~ I     ��������  0 getcurrentpath getCurrentPath��  ��    m    ��
�� 
alis } o      ���� 0 currentpath currentPath��  ��   z  � � � l     ��������  ��  ��   �  � � � l  
  ����� � I   
 ��������  0 activateiterms activateiTerms��  ��  ��  ��   �  � � � l    ����� � I    �� �����  0 setwindowtitle setWindowTitle �  ��� � m     � � � � �  T y S t r i n g s   D e m o��  ��  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l     �� � ���   �   cd to repo root path    � � � � *   c d   t o   r e p o   r o o t   p a t h �  � � � l   % ����� � I    %�� ����� 0 
runcommand 
runCommand �  ��� � b    ! � � � b     � � � m     � � � � �  c d   � l    ����� � n     � � � 1    ��
�� 
strq � n     � � � 1    ��
�� 
psxp � o    ���� 0 currentpath currentPath��  ��   � m      � � � � �  . . /��  ��  ��  ��   �  � � � l  & , ����� � I   & ,�� ����� 0 
runcommand 
runCommand �  ��� � m   ' ( � � � � � 0 s o u r c e   v e n v / b i n / a c t i v a t e��  ��  ��  ��   �  � � � l  - 3 ����� � I   - 3�� ����� 0 
runcommand 
runCommand �  ��� � m   . / � � � � � " c d   t e s t s / e x a m p l e /��  ��  ��  ��   �  � � � l  4 9 ����� � I   4 9�������� 	0 clear  ��  ��  ��  ��   �  � � � l  : @ ����� � I   : @�� ����� 0 
runcommand 
runCommand �  ��� � m   ; < � � � � � > t t y r e c   . . / . . / r e s o u r c e / r e c o r d i n g��  ��  ��  ��   �  � � � l  A F ����� � I  A F�� ���
�� .sysodelanull��� ��� nmbr � m   A B � � ?�      ��  ��  ��   �  � � � l  G Z ����� � I   G Z�� ����� 00 runtystringssubcommand runTyStringsSubCommand �  � � � m   H K � � � � �  g e n e r a t e �  ��� � J   K V � �  � � � m   K N � � � � � ( $ ( f i n d   .   - n a m e   \ * . m ) �  � � � m   N Q � � � � �  - o �  ��� � m   Q T � � � � � , e n . l p r o j   z h - H a n s . l p r o j��  ��  ��  ��  ��   �  � � � l  [ ` ����� � I  [ `�� ���
�� .sysodelanull��� ��� nmbr � m   [ \���� ��  ��  ��   �  � � � l  a f ����� � I   a f�������� 	0 clear  ��  ��  ��  ��   �  � � � l  g � ����� � I   g ��� ����� 00 runtystringssubcommand runTyStringsSubCommand �  � � � m   h k � � � � �  t r a n s l a t e �  ��� � J   k � � �  � � � m   k n � � � � � > s t r i n g s / b a s e _ t r a n s l a t o r . s t r i n g s �  � � � m   n q � � � � � J z h - H a n s . l p r o j / b a s e _ t r a n s l a t o r . s t r i n g s �  � � � m   q t � � � � �  - - d s t - l a n g �  � � � m   t w � � � � �  z h �  � � � m   w z � � � � �  - - s r c - l a n g �  ��� � m   z } � � � � �  e n��  ��  ��  ��  ��   �  �  � l  � ����� I  � �����
�� .sysodelanull��� ��� nmbr m   � ����� ��  ��  ��     l  � ����� I   � ��������� 	0 clear  ��  ��  ��  ��    l  � ����� I   � ���	���� 00 runtystringssubcommand runTyStringsSubCommand	 

 m   � � �  d i f f �� J   � �  m   � � � * s t r i n g s / d i f f 1 . s t r i n g s �� m   � � � * s t r i n g s / d i f f 2 . s t r i n g s��  ��  ��  ��  ��    l  � ���~ I  � ��}�|
�} .sysodelanull��� ��� nmbr m   � ��{�{ �|  �  �~    l  � ��z�y I   � ��x�w�v�x 	0 clear  �w  �v  �z  �y    l  � � �u�t  I   � ��s!�r�s 00 runtystringssubcommand runTyStringsSubCommand! "#" m   � �$$ �%%  l i n t# &�q& J   � �'' (�p( m   � �)) �** ( s t r i n g s / l i n t . s t r i n g s�p  �q  �r  �u  �t   +,+ l  � �-�o�n- I  � ��m.�l
�m .sysodelanull��� ��� nmbr. m   � ��k�k �l  �o  �n  , /0/ l  � �1�j�i1 I   � ��h2�g�h 0 
runcommand 
runCommand2 3�f3 m   � �44 �55  e x i t�f  �g  �j  �i  0 676 l  � �8�e�d8 I  � ��c9�b
�c .sysodelanull��� ��� nmbr9 m   � �:: ?�      �b  �e  �d  7 ;<; l  � �=�a�`= I   � ��_>�^�_ 0 
runcommand 
runCommand> ?�]? b   � �@A@ b   � �BCB m   � �DD �EE  c d  C l  � �F�\�[F n   � �GHG 1   � ��Z
�Z 
strqH n   � �IJI 1   � ��Y
�Y 
psxpJ o   � ��X�X 0 currentpath currentPath�\  �[  A m   � �KK �LL  . . /�]  �^  �a  �`  < MNM l  � �O�W�VO I   � ��UP�T�U 0 
runcommand 
runCommandP Q�SQ m   � �RR �SS  d e a c t i v a t e�S  �T  �W  �V  N TUT l  � �V�R�QV I   � ��PW�O�P 0 
runcommand 
runCommandW X�NX m   � �YY �ZZ 8 t t y g i f   r e s o u r c e / r e c o r d i n g   - f�N  �O  �R  �Q  U [\[ l  � �]�M�L] I   � ��K^�J�K 0 
runcommand 
runCommand^ _�I_ m   � �`` �aa B m v   t t y . g i f   r e s o u r c e / t y s t r i n g s . g i f�I  �J  �M  �L  \ bcb l     �H�G�F�H  �G  �F  c ded l     �Efg�E  f   clean   g �hh    c l e a ne iji l  k�D�Ck I   �Bl�A�B 0 
runcommand 
runCommandl m�@m m  nn �oo : r m   - r f   t e s t s / e x a m p l e / e n . l p r o j�@  �A  �D  �C  j pqp l 	r�?�>r I  	�=s�<�= 0 
runcommand 
runCommands t�;t m  
uu �vv D r m   - r f   t e s t s / e x a m p l e / z h - H a n s . l p r o j�;  �<  �?  �>  q wxw l     �:�9�8�:  �9  �8  x yzy l     �7{|�7  { ( " ------- TyStrings Helper -------    | �}} D   - - - - - - -   T y S t r i n g s   H e l p e r   - - - - - - -  z ~~ l     �6�5�4�6  �5  �4   ��� i     ��� I      �3�2�1�3 (0 rungeneratecommand runGenerateCommand�2  �1  � l     �0�/�.�0  �/  �.  � ��� l     �-�,�+�-  �,  �+  � ��� i    ��� I      �*��)�* 00 runtystringssubcommand runTyStringsSubCommand� ��� o      �(�( 0 
subcommand  � ��'� o      �&�& 0 args  �'  �)  � k     @�� ��� I     �%��$�% 0 typingstring typingString� ��#� m    �� ���  t y s�#  �$  � ��� I    �"��!�" .0 typingstringwithdelay typingStringWithDelay� ��� m    	�� ���  t r i n g s  � �� � m   	 
��  �   �!  � ��� I    ���� 0 typingstring typingString� ��� b    ��� o    �� 0 
subcommand  � m    �� ���   �  �  � ��� Y    7������ I   & 2���� .0 typingstringwithdelay typingStringWithDelay� ��� b   ' -��� n   ' +��� 4   ( +��
� 
cobj� o   ) *�� 0 i  � o   ' (�� 0 args  � m   + ,�� ���   � ��� m   - .�� ?�z�G�{�  �  � 0 i  � m    �� � I   !���
� .corecnte****       ****� o    �� 0 args  �  �  � ��� l  8 8����  �   typing '\n'   � ���    t y p i n g   ' \ n '� ��� I   8 >���� 0 typingstring typingString� ��� m   9 :�� ���  
�  �  � ��
� l  ? ?�	���	  �  �  �
  � ��� l     ����  �  �  � ��� l     ����  �   ------- Core -------    � ��� ,   - - - - - - -   C o r e   - - - - - - -  � ��� l     ��� �  �  �   � ��� i    ��� I      ������� 0 typingstring typingString� ���� o      ���� 0 content  ��  ��  � I     ������� .0 typingstringwithdelay typingStringWithDelay� ��� o    ���� 0 content  � ���� m    �� ?���������  ��  � ��� l     ��������  ��  ��  � ��� i    ��� I      ������� .0 typingstringwithdelay typingStringWithDelay� ��� o      ���� 0 content  � ���� o      ���� 0 dy  ��  ��  � O     B��� O    A��� k    @�� ��� r    ��� l   ������ n    ��� 7   ����
�� 
cha � m    ���� � l   ������ n    ��� 1    ��
�� 
leng� o    ���� 0 content  ��  ��  � o    ���� 0 content  ��  ��  � o      ���� 0 charlist charList� ���� X    @����� k   , ;�� ��� I  , 5�����
�� .Itrmsntxnull���     obj ��  � ����
�� 
Text� o   . /���� 0 char  � �����
�� 
Wtnl� m   0 1��
�� savono  ��  � ���� I  6 ;�����
�� .sysodelanull��� ��� nmbr� o   6 7���� 0 dy  ��  ��  �� 0 char  � o     ���� 0 charlist charList��  � n    	��� 1    	��
�� 
Wcsn� 1    ��
�� 
Crwn� m       �                                                                                  ITRM  alis    @  	Macintosh                  �6�]H+  ٣�	iTerm.app                                                      1G��lے        ����  	                Applications    �6.�      �lk    ٣�  !Macintosh:Applications: iTerm.app    	 i T e r m . a p p   	 M a c i n t o s h  Applications/iTerm.app  / ��  �  l     ��������  ��  ��    i     I      ������ 0 
runcommand 
runCommand �� o      ���� 0 command  ��  ��   O     	
	 O     I   ����
�� .Itrmsntxnull���     obj ��   ����
�� 
Text o    ���� 0 command  ��   n    	 1    	��
�� 
Wcsn 1    ��
�� 
Crwn
 m     �                                                                                  ITRM  alis    @  	Macintosh                  �6�]H+  ٣�	iTerm.app                                                      1G��lے        ����  	                Applications    �6.�      �lk    ٣�  !Macintosh:Applications: iTerm.app    	 i T e r m . a p p   	 M a c i n t o s h  Applications/iTerm.app  / ��    l     ��������  ��  ��    i     I      �������� 	0 clear  ��  ��   k       I     ������ 0 
runcommand 
runCommand �� m     � 
 c l e a r��  ��   �� I   �� ��
�� .sysodelanull��� ��� nmbr  m    !! ?���������  ��   "#" l     ��������  ��  ��  # $%$ i    &'& I      ��(���� 0 isapprunning isAppRunning( )��) o      ���� 0 appname appName��  ��  ' O    *+* E    ,-, l   	.����. n    	/0/ 1    	��
�� 
pnam0 2   ��
�� 
prcs��  ��  - o   	 
���� 0 appname appName+ m     11�                                                                                  sevs  alis    �  	Macintosh                  �6�]H+  ٣}System Events.app                                              ܠ��Ó�        ����  	                CoreServices    �6.�      ��#(    ٣}٣|٣{  :Macintosh:System: Library: CoreServices: System Events.app  $  S y s t e m   E v e n t s . a p p   	 M a c i n t o s h  -System/Library/CoreServices/System Events.app   / ��  % 232 l     ��������  ��  ��  3 454 i    676 I      ��8����  0 setwindowtitle setWindowTitle8 9��9 o      ���� 	0 title  ��  ��  7 I     
��:���� 0 
runcommand 
runCommand: ;��; b    <=< b    >?> m    @@ �AA  e c h o   - e   " \ 0 3 3 ] ;? o    ���� 	0 title  = m    BB �CC 
 \ 0 0 7 "��  ��  5 DED l     ��������  ��  ��  E FGF i     #HIH I      ��������  0 activateiterms activateiTerms��  ��  I Z     JK��LJ I     ��M���� 0 isapprunning isAppRunningM N��N m    OO �PP 
 i T e r m��  ��  K O   	 QRQ I   ������
�� .miscactvnull��� ��� null��  ��  R m   	 
SS�                                                                                  ITRM  alis    @  	Macintosh                  �6�]H+  ٣�	iTerm.app                                                      1G��lے        ����  	                Applications    �6.�      �lk    ٣�  !Macintosh:Applications: iTerm.app    	 i T e r m . a p p   	 M a c i n t o s h  Applications/iTerm.app  / ��  ��  L I   ��T��
�� .miscactvnull��� ��� nullT m    UU�                                                                                  ITRM  alis    @  	Macintosh                  �6�]H+  ٣�	iTerm.app                                                      1G��lے        ����  	                Applications    �6.�      �lk    ٣�  !Macintosh:Applications: iTerm.app    	 i T e r m . a p p   	 M a c i n t o s h  Applications/iTerm.app  / ��  ��  G VWV l     ��������  ��  ��  W XYX i   $ 'Z[Z I      ��������  0 getcurrentpath getCurrentPath��  ��  [ O     \]\ L    ^^ n    _`_ m   	 ��
�� 
ctnr` l   	a����a I   	��b��
�� .earsffdralis        afdrb  f    ��  ��  ��  ] m     cc�                                                                                  MACS  alis    l  	Macintosh                  �6�]H+  ٣}
Finder.app                                                     �9J�H��        ����  	                CoreServices    �6.�      �HA    ٣}٣|٣{  3Macintosh:System: Library: CoreServices: Finder.app    
 F i n d e r . a p p   	 M a c i n t o s h  &System/Library/CoreServices/Finder.app  / ��  Y d��d l     ��������  ��  ��  ��       ��efghijklmnop��  e ��������������~�}�|�{�� (0 rungeneratecommand runGenerateCommand�� 00 runtystringssubcommand runTyStringsSubCommand�� 0 typingstring typingString�� .0 typingstringwithdelay typingStringWithDelay�� 0 
runcommand 
runCommand�� 	0 clear  � 0 isapprunning isAppRunning�~  0 setwindowtitle setWindowTitle�}  0 activateiterms activateiTerms�|  0 getcurrentpath getCurrentPath
�{ .aevtoappnull  �   � ****f �z��y�xqr�w�z (0 rungeneratecommand runGenerateCommand�y  �x  q  r  �w hg �v��u�tst�s�v 00 runtystringssubcommand runTyStringsSubCommand�u �ru�r u  �q�p�q 0 
subcommand  �p 0 args  �t  s �o�n�m�o 0 
subcommand  �n 0 args  �m 0 i  t 
��l��k��j�i����l 0 typingstring typingString�k .0 typingstringwithdelay typingStringWithDelay
�j .corecnte****       ****
�i 
cobj�s A*�k+ O*�jl+ O*��%k+ O k�j kh *��/�%�l+ [OY��O*�k+ OPh �h��g�fvw�e�h 0 typingstring typingString�g �dx�d x  �c�c 0 content  �f  v �b�b 0 content  w ��a�a .0 typingstringwithdelay typingStringWithDelay�e *��l+ i �`��_�^yz�]�` .0 typingstringwithdelay typingStringWithDelay�_ �\{�\ {  �[�Z�[ 0 content  �Z 0 dy  �^  y �Y�X�W�V�Y 0 content  �X 0 dy  �W 0 charlist charList�V 0 char  z  �U�T�S�R�Q�P�O�N�M�L�K�J�I
�U 
Crwn
�T 
Wcsn
�S 
cha 
�R 
leng
�Q 
kocl
�P 
cobj
�O .corecnte****       ****
�N 
Text
�M 
Wtnl
�L savono  �K 
�J .Itrmsntxnull���     obj 
�I .sysodelanull��� ��� nmbr�] C� ?*�,�, 6�[�\[Zk\Z��,2E�O #�[��l kh *���� O�j [OY��UUj �H�G�F|}�E�H 0 
runcommand 
runCommand�G �D~�D ~  �C�C 0 command  �F  | �B�B 0 command  } �A�@�?�>
�A 
Crwn
�@ 
Wcsn
�? 
Text
�> .Itrmsntxnull���     obj �E � *�,�, 	*�l UUk �=�<�;��:�= 	0 clear  �<  �;    � �9!�8�9 0 
runcommand 
runCommand
�8 .sysodelanull��� ��� nmbr�: *�k+ O�j l �7'�6�5���4�7 0 isapprunning isAppRunning�6 �3��3 �  �2�2 0 appname appName�5  � �1�1 0 appname appName� 1�0�/
�0 
prcs
�/ 
pnam�4 � 	*�-�,�Um �.7�-�,���+�.  0 setwindowtitle setWindowTitle�- �*��* �  �)�) 	0 title  �,  � �(�( 	0 title  � @B�'�' 0 
runcommand 
runCommand�+ *�%�%k+ n �&I�%�$���#�&  0 activateiterms activateiTerms�%  �$  �  � O�"S�!�" 0 isapprunning isAppRunning
�! .miscactvnull��� ��� null�# *�k+  � *j UY �j o � [������   0 getcurrentpath getCurrentPath�  �  �  � c��
� .earsffdralis        afdr
� 
ctnr� � )j �,EUp �������
� .aevtoappnull  �   � ****� k    ��  y��  ���  ���  ���  ���  ���  ���  ���  ���  ���  ���  ���  ���  ��� �� �� �� �� �� +�� /�� 6�� ;�� M�� T�� [�� i�� p��  �  �  �  � +���� �� ��� �� � �� � �� � � � �� � � � � � � ��
$)4DKRY`nu�  0 getcurrentpath getCurrentPath
� 
alis� 0 currentpath currentPath�  0 activateiterms activateiTerms�  0 setwindowtitle setWindowTitle
� 
psxp
� 
strq� 0 
runcommand 
runCommand� 	0 clear  
� .sysodelanull��� ��� nmbr� 00 runtystringssubcommand runTyStringsSubCommand�
 �*j+  �&E�O*j+ O*�k+ O*���,�,%�%k+ 
O*�k+ 
O*�k+ 
O*j+ O*�k+ 
O�j O*a a a a mvl+ Olj O*j+ O*a a a a a a a a vl+ Olj O*j+ O*a a a  lvl+ Olj O*j+ O*a !a "kvl+ Olj O*a #k+ 
O�j O*a $��,�,%a %%k+ 
O*a &k+ 
O*a 'k+ 
O*a (k+ 
O*a )k+ 
O*a *k+ 
 ascr  ��ޭ