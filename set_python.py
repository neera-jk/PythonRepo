# text = """Education is not the learning of facts
# but the training of the mind to think
# - Albert Einstein"""

# prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# # Add your code here.
# words = set(text.split())
# # print(words)

# preps_used = words & prepositions
# print(preps_used)


favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.
suggestions = favourites - basket
print(suggestions)