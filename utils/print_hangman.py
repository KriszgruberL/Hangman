class PrintHangman() :
    title_hangman = """
+-----------------------------------------------------------------------+
|    _                                                     _______      |
|   | |                                                   |/      |     |
|   | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __         |      (_)    |
|   | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \        |      \|/    |
|   | | | | (_| | | | | (_| | | | | | | (_| | | | |       |       |     |
|   |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|       |      / \    |
|                       __/ |                             |             |
|                      |___/                             _|____         |
+-----------------------------------------------------------------------+\n"""

    ascii_hangman = [
        """
              _______
             |/      |
             |      
             |      
             |      
             |      
             |
         _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |      
             |       
             |      
             |
            _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |       |
             |       |
             |      
             |
            _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |      \|
             |       |
             |      
             |
            _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      
             |
            _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / 
             |
            _|___
        """,
        """
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / \ 
             |
            _|___
        """
    ]