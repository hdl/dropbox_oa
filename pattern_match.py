import copy
def patternMatches(p,s):

    #mapping is a dictionary that maps a character in p to a
    #substring of s
    def helper(p,s,mapping):
        #pattern is longer than provided string. not possible

        print mapping
        print "p is " + p
        print "s is " + s

        if len(p) > len(s):
            return False
        #both pattern and string ran out at the same time. yay
        if len(p) == 0 and len(s) == 0:
            return True
        #pattern ran out but not the string. boo
        if len(p) == 0:
            return False

        #current key we're considering
        key = p[0]
        #if key is already included in our mapping, check if s indeed
        #begins with the value of this key. if not, then we can't
        #continue with this particular set of mapping
        if key in mapping:
            mapped = mapping[key]
            if s.startswith(mapped):
                return helper(p[1:],s[len(mapped):],mapping)
            else:
                return False
        #if key doesn't exist in our mapping, then we brute-force-ly
        #guess all substrings of s to be the value of this key and
        #recursively call patternMatches on each map
        else:
            if len(p)==1:  # the last char in p, can map to anything
                return True
            for i in range(1,len(s)+1):
                guess = s[:i]
                #this guess_mapping is very important. it allows us to
                #try different keys in the recursive calls w/o affecting
                #our original mapping
                guess_mapping = copy.copy(mapping)
                guess_mapping[key] = guess
                if helper(p[1:],s[len(guess):],guess_mapping):
                   return True

        return False

    return helper(p,s,{})
if __name__ == "__main__":
    print patternMatches("abc", "redblueredblue")
