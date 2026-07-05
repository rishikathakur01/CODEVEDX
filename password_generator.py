import secrets  # 'random' ki jagah 'secrets' use karne se security aur badh jaati hai (Unique Touch)
import string

def generate_custom_password(pwd_len=12, include_caps=True, include_small=True, include_nums=True, include_syms=True):
    """Function to assemble characters and build a randomized string"""
    char_pool = ""
    if include_caps:
        char_pool += string.ascii_uppercase
    if include_small:
        char_pool += string.ascii_lowercase
    if include_nums:
        char_pool += string.digits
    if include_syms:
        char_pool += string.punctuation

    # Fallback if everything is false
    if not char_pool:
        char_pool = string.ascii_letters + string.digits

    # Cryptographically secure random selection
    secure_pwd = ''.join(secrets.choice(char_pool) for _ in range(pwd_len))
    return secure_pwd

def check_pwd_complexity(pwd_str):
    """Function to grade the strength of the generated password"""
    pwd_len = len(pwd_str)
    has_caps = any(c.isupper() for c in pwd_str)
    has_small = any(c.islower() for c in pwd_str)
    has_nums = any(c.isdigit() for c in pwd_str)
    has_syms = any(c in string.punctuation for c in pwd_str)
    
    total_criteria = sum([has_caps, has_small, has_nums, has_syms])
    
    if pwd_len >= 12 and total_criteria == 4:
        return "Excellent 🟢 (Highly Secure)"
    elif pwd_len >= 8 and total_criteria >= 3:
        return "Good 🟡 (Moderate Protection)"
    else:
        return "Vulnerable 🔴 (Easy to Crack)"

if __name__ == "__main__":
    print("=" * 45)
    print("       SECURE PASSWORD COMPOSER TOOL       ")
    print("=" * 45)
    
    try:
        user_choice_len = int(input("Enter desired password length (e.g., 12, 16): "))
    except ValueError:
        print("⚠️ Invalid input! System choosing default length of 12.")
        user_choice_len = 12

    # Configurations
    allow_caps = True      
    allow_small = True
    allow_nums = True
    allow_syms = True

    print(f"\nConstructing your password with {user_choice_len} characters...")
    
    # Process
    generated_output = generate_custom_password(
        pwd_len=user_choice_len, 
        include_caps=allow_caps, 
        include_small=allow_small, 
        include_nums=allow_nums, 
        include_syms=allow_syms
    )
    
    safety_label = check_pwd_complexity(generated_output)
    
    # Final Result
    print("\n" + "*" * 45)
    print(f"Resulting Password : {generated_output}")
    print(f"Security Level     : {safety_label}")
    print("*" * 45)
