import re
import os

class Validation:
    
    def text_validation(text:str,replacement:dict) -> str:
        """Replace the invalid word with the valid one that both are in the replacement dictionary
        Args:
            text: The input text string.
            replacement: {invalid_word:valid_substitute}
        Returns:
            The modified text with replacement made.
        """
        regex=['(','|'.join(replacement.keys()),')']
        new_regex=''.join(regex)
        return re.sub(new_regex, lambda match: replacement[match.group()], text)

    def email_validation(email:str) -> bool :
        regex=r'([\w\d-]+)@([\w\d]+)([\.\w+])'
        if re.match(regex,email):
            return True
        return False
    
    def check_directory(dir:str) -> bool:
        if os.path.exists(dir):
            return True
        raise FileNotFoundError("Entered directory doesn't exist!!!")