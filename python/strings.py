msg1 = 'Cisco Switch'
print('Input msg1 : ', msg1)

msg1Len = len(msg1)
print('msg1 length : ',msg1Len)

# Display Character in a array index
print('1st Char : ', msg1[0])
print('12th Char : ', msg1[msg1Len-1]) # since starting from index starts from 0, it goes till n-1
print('Last Char : ', msg1[-1])

# Finding what is the index number of character
print('Index of Character "C" is ', msg1.index("C")); # Case sensitive
print('Index of Character "c" is ', msg1.index("c")); # Case sensitive & returns the index of first occurence

# Finding how many occurence of character
print('Count of Character "C" is ', msg1.count("C")); # Case sensitive & returns the index of first occurence
print('Count of Character "c" is ', msg1.count("c")); # Case sensitive & returns the index of first occurence

# Finding how many occurence of character
print('Finding "sco"', msg1.find("sco")); # Case sensitive & returns start index number of string
print('Finding "Swi"', msg1.find("Swi")); # Case sensitive & returns start index number of string

# Formatting Variable
print('Converting variables to lower case : ', msg1.lower());
print('Converting variables to lower case : ', msg1.upper());

# Pre-Checking sentence with characters
print('Starts with "C"', msg1.startswith("C"));
print('Starts with "h"', msg1.endswith("h"));
print('Starts with "o"', msg1.endswith("o"));


msg2 = '          _$Hello World____        '
print('Remove leading & ending whitespace in String : ', msg2.strip()); 
print('Remove all $ in Strings : ', msg2.strip("$")); 
print('Remove all whitespace in Strings : ', msg2.replace(" ", "")); 

msg3 = "IoT Core, CodeCommit, CodeBuild, CodeDeploy, CodeArtifactory"
print('Returns all the elements delimited by "," in Lists : ', msg3.split(",")); # Returns in list data type

print("_".join(msg3)) # Outputs : I_o_T_ _C_o_r_e_,_ _C_o_d_e_C_o_m_m_i_t_,_ _C_o_d_e_B_u_i_l_d_,_ _C_o_d_e_D_e_p_l_o_y_,_ _C_o_d_e_A_r_t_i_f_a_c_t_o_r_y
print(msg1 + msg3)
print(msg1 *3)
print("i" in msg1)

msg4 = 'Cisco Model: %s, %d WAN Slots, IOS %f' % ('2600F', 10, 12.54) #Cisco Model: 2600F, 10 WAN Slots, IOS 12.540000
print(msg4)
msg4 = 'Cisco Model: %s, %d WAN Slots, IOS %.2f' % ('2600F', 10, 12.54)
print(msg4)
msg4 = 'Cisco Model: %s, %d WAN Slots, IOS %.f' % ('2600F', 10, 12.54)
print(msg4)

# Formatting Strings
msg4 = 'Cisco Model: {}, {} WAN Slots, IOS {}' 
print(msg4.format('2600F', 10, 12.54))
msg4 = 'Cisco Model: {0}, {1} WAN Slots, IOS {2}' 
print(msg4.format('2600F', 10, 12.54))

# F Strings
model = '2600F'
slots = 10
ios = 12.54
print(f'Cisco Model: {model}, {slots} WAN Slots, IOS {ios}')
print(f'Cisco Model: {model}, {slots*2} WAN Slots, IOS {ios}')
print(f'Cisco Model: {model.lower()}, {slots*2} WAN Slots, IOS {ios}')

msg5 = 'Reply from 146.112.51.52: bytes=32 time=361ms TTL=53'
print(msg5.find('14'))
print(msg5.find(':'))
print('IP Address: ', msg5[11:24])
print(msg5.find('='))
print('Bytes Sent: ', msg5[32:34])

msg5 = '0123456789'
print(msg5[::2])
print(msg5[1::2])
print(msg5[1:7:2])




