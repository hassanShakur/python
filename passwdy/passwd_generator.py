from random import choice, randint, shuffle

alphas = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D','F','G','H','H','J','K','L','Z','X','C','V','B','N','M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

numbers = ['1','2','3','4','5','6','7','8','9','0']
betas = ['!', '@','#','$','%','^','&','*','(',')','_']

def generate_passwd():
    alpha_rand = randint(8, 14)
    num_rand = randint(3, 5)
    beta_rand = randint(3, 6)

    alpha_count = [choice(alphas) for _ in range(alpha_rand)]
    num_count = [choice(numbers) for _ in range(num_rand)]
    beta_count = [choice(betas) for _ in range(beta_rand)]

    passwd = alpha_count + num_count + beta_count
    shuffle(passwd)
    passwd = ''.join(passwd)
    return passwd
