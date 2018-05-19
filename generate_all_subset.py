def get_substring(substr,s,pos,cur_subset):
    # type: (object) -> object

    if(pos == len(s)):
        #print("length <=1 for %s,with length =%d" %(s,len(s)))
        substr.append(cur_subset)
        return

    get_substring(substr,s,pos+1,cur_subset)
    #Not include x
    get_substring(substr, s, pos + 1, cur_subset + s[pos])
    
def generate_all_subsets(s):
    substr = []
    res = get_substring(substr,s,0,"")
    return substr

    #print("substr =",substr)
