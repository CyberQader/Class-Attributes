class Member:
    not_allowed_names = ['Hell','Shit','BB']
    users_num = 0
    def __init__(self,first_name,middle_name,last_name,gender):
       self.fname = first_name
       self.mname = middle_name
       self.lname = last_name
       self.gender = gender
       Member.users_num += 1
    def full_name(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError('Name Not Allowed')
        else:
            return f'{self.fname}{self.mname}{self.lname}'
    def name_with_title(self):
        if self.gender == 'Male':
           return f'Hello Mr{self.fname}'
        elif self.gender == 'Female':
            return f'Hello Miss{self.fname}'
        else:
            return f'Hello {self.fname}'
    def get_all_info(self):
        return f'{self.name_with_title(),'Your Full Name Is' : {self.full_name()}}'
    def delete_user(self):
        Member.users_num -=1
        return f'User{self.fname} Is Deleted!!'
print(Member.users_num)
member_one = Member('abood','abd0','iyad','shbika')
member_tow = Member('abood','abd0','iyad','shbika')
member_three = Member('abood','abd0','iyad','shbika')
member_four= Member('hell','Shit','iyad','shbika')
print(Member.users_num)
print(member_one)
