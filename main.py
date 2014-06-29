import psidialogs

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
        
        return tab_str.expandtabs(int(tab_val))
        
    
    
        


if __name__ == "__main__":
    input_str=psidialogs.ask_string(message='Enter String.', default='', title='String Input')
    str_a1=STRING(input_str)
    
    while True:
        str_methods=psidialogs.choice(choices=['capital()','center()','count()','encode()_decode()','endswith()','expandtabs()','Exit'], message='Make a choice.', default=None, title='Strings')
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
            

        elif str_methods=='Exit':
            print 'exited'
            exit(0)

        else:
            print 'Enter correct choice '
            
            
            
    
    
