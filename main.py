import psidialogs
from string import maketrans

class STRING():
    def __init__(self,val):
        self.val=val
        print 'my val'
        
    def str_capital(self):
        #self.val=pop
        return self.val.capitalize()
    
    def str_center(self):
        width=psidialogs.ask_string(message='Enter Width.', default='', title='Center()')
        fill=psidialogs.ask_string(message='Enter Fillchar.', default='', title='Center()')
        return self.val.center(int(width),str(fill))
    
    def str_count(self):
        sub_str=psidialogs.ask_string(message='Enter String to be searched.', default='', title='count()')
        start_pos=psidialogs.ask_string(message='Enter starting position.', default='', title='count()')
        end_pos=psidialogs.ask_string(message='Enter ending position.', default='', title='count()')
        return self.val.count(sub_str,int(start_pos),int(end_pos))
    
    def str_encode_decode(self):
        choice=psidialogs.choice(choices=['Encode','Decode'], message='Pick something.', default=None, title='Encode/Decode')
        if choice=='Encode':
            encode_list=psidialogs.choice(choices=['base64','bz2','hex','quopri','uu','zlib'], message='Pick something.', default=None, title='Encode choice')
            return self.val.encode(encode_list,'strict')
        
        else:
            decode_list=psidialogs.choice(choices=['base64','bz2','hex','quopri','uu','zlib'], message='Pick something.', default=None, title='Encode choice')
            return self.val.decode(decode_list,'strict')

    def str_endswith(self):
        suffix=psidialogs.ask_string(message='Enter String .', default='', title='endswith()')
        start_pos=psidialogs.ask_string(message='Enter starting position.', default='', title='endswith()')
        end_pos=psidialogs.ask_string(message='Enter ending position.', default='', title='endswith()')
        return self.val.endswith(suffix,int(start_pos),int(end_pos))


    def str_expandtabs(self):
        tab_str=psidialogs.ask_string(message='Enter String and put\t.', default='', title='expandtabs()')
        tab_val=psidialogs.ask_string(message='Enter Tab value.', default='', title='expandtabs()')
        from string import maketrans
        return tab_str.expandtabs(int(tab_val))

    def str_find(self):
        sub_str=psidialogs.ask_string(message='Enter Substring', default='', title='index()')
        start_point=psidialogs.ask_string(message='Enter Starting point', default='', title='find()')
        end_point=psidialogs.ask_string(message='Enter Starting point.', default='', title='find()')
        
        return self.val.find(sub_str,int(start_point),int(end_point))
    
    def str_index(self):
        sub_str=psidialogs.ask_string(message='Enter Substring', default='', title='index()')
        start_point=psidialogs.ask_string(message='Enter Starting point', default='', title='index()')
        end_point=psidialogs.ask_string(message='Enter Starting point.', default='', title='index()')
        return self.val.index(sub_str,int(start_point),int(end_point))
        

    def str_isalnum(self):
        return self.val.isalnum()

    def str_isalpha(self):
        return self.val.isalpha()

    def str_isdigit(self):
        return self.val.isdigit()

    def str_isnumeric(self):
        return self.val.isnumeric()

    def str_isspace(self):
        return self.val.isspace()

    def str_islower(self):
        return self.val.islower()

    def str_istitle(self):
        return self.val.istitle()

    def str_isupper(self):
        return self.val.isupper()

    def str_join(self):
        str_join=psidialogs.ask_string(message='Enter join string.', default='', title='join()')
        str_seq=psidialogs.ask_string(message='Enter sequence(tuple).', default='', title='join()')
        return self.str_join.join(str_seq)

    def str_len(self):
        return self.val.len()

    def str_ljust(self):
        width=psidialogs.ask_string(message='Enter width.', default='', title='ljust()')
        fillchar=psidialogs.ask_string(message='Enter sttring to fill .', default='', title='ljust()')
        return self.str_join.join(str_seq)

    def str_lower(self):
        return self.val.lower()
    

    def str_maketrans(self):
        intab=psidialogs.ask_string(message='Enter vowels', default='', title='maketrans()')
        outab=psidialogs.ask_string(message='Enter vowels replacement', default='', title='maketrans()')
        maketrans_obj= maketrans(intab,outab)
        return self.val.maketrans(maketrans_obj)
    
    
    def str_max(self):
        return max(self.val)
    
    def str_min(self):
        return min(self.val)    


if __name__ == "__main__":
    input_str=psidialogs.ask_string(message='Enter String.', default='', title='String Input')
    str_a1=STRING(input_str)
    
    while True:
        str_methods=psidialogs.choice(choices=['capital()','center()','count()',\
        'encode()_decode()','endswith()','expandtabs()','find()','index()',\
        'isalnum()','isalpha()','isdigit()','isnumeric()',\
        'isspace()','istitle()','isupper()',\
        'join()','len()','ljust()','lower()','maketrans()','max()','min()','Exit'], message='Make a choice.', default=None, title='Strings')
        if str_methods=='capital()':
            print str_a1.str_capital()
        
        elif str_methods=='center()':
            print str_a1.str_center()

        elif str_methods=='count()':
            print str_a1.str_count()
            

        elif str_methods=='encode()_decode()':
            print str_a1.str_encode_decode()

        elif str_methods=='endswith()':
            print str_a1.str_endswith()

        elif str_methods=='expandtabs()':
            print str_a1.str_expandtabs()

        elif str_methods=='find()':
            print str_a1.str_find()

        elif str_methods=='index()':
            print str_a1.str_index()

        elif str_methods=='isalnum()':
            print str_a1.str_isalnum()

        elif str_methods=='isalpha()':
            print str_a1.str_isalpha()            

        elif str_methods=='isdigit()':
            print str_a1.str_isdigit()
            
        elif str_methods=='isnumeric()':
            print str_a1.str_isdigit()

        elif str_methods=='istitle':
            print str_a1.str_isdigit()

        elif str_methods=='isspace()':
            print str_a1.str_isdigit()

        elif str_methods=='islower()':
            print str_a1.str_isdigit()

        elif str_methods=='isupper()':
            print str_a1.str_isdigit()

###########
        elif str_methods=='join()':
            print str_a1.str_join()()

        elif str_methods=='len()':
            print str_a1.str_len()

        elif str_methods=='ljust()':
            print str_a1.str_ljust()

        elif str_methods=='lower()':
            print str_a1.str_lower()

        elif str_methods=='maketrans()':
            print str_a1.str_maketrans()

        elif str_methods=='max()':
            print str_a1.str_max()

        elif str_methods=='min()':
            print str_a1.str_min()
            

        elif str_methods=='Exit':
            print 'exited'
            exit(0)

        else:
            print 'Enter correct choice '
            
            
            
    
    
