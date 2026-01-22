import pytest

class TestCreditCardValidator:
    
    """ Visa Card """
    def test_valid_visa(self):
        """Test valid visa"""
        assert credit_card_validator("4463125740262107") == True
    def test_invalid_visa(self):
        """Test invalid visa"""
        assert credit_card_validator("4463125740262109") == False
    def test_invalid_visa_length17(self):
        """Test invalid length valid visa of 17"""
        assert credit_card_validator("43702660504138936") == False
    def test_invalid_visa_length15(self):
        """Test invalid length valid visa of 15"""
        assert credit_card_validator("424422687364335") == False



    """ Valid Master Card """
    def test_valid_masterCard_51(self):
        """Test valid master card starting with 51"""
        assert credit_card_validator("5105105105105100") == True
    def test_valid_masterCard_between51and55(self):
        """Test valid master card between 51-55"""
        assert credit_card_validator("5424180279791732") == True
    def test_valid_masterCard_55(self):
        """Test valid master card starting with 55"""
        assert credit_card_validator("5555555555554444") == True
    def test_valid_masterCard_between2221and2720(self):
        """Test valid master card between 2221-2720"""
        assert credit_card_validator("2223003122003222") == True

    """ Invalid Master Card """
    def test_invalid_length_masterCard17(self):
        """Test invalid length valid master card 17 digits"""
        assert credit_card_validator("53111934264215646") == False
    def test_invalid_length_masterCard15(self):
        """Test invalid length valid master card 15 digits"""
        assert credit_card_validator("529153543723745") == False
    def test_invalid_masterCard(self):
        """Test invalid master card"""
        assert credit_card_validator("5311193426421566") == False



    """ Valid American """
    def test_valid_american_34(self):
        """Test valid american card starting with 34"""
        assert credit_card_validator("340000000000009") == True
    def test_valid_american_37(self):
        """Test valid american card starting with 37"""
        assert credit_card_validator("378282246310005") == True

    """ Invalid American """
    def test_invalid_length_american_2(self):
        """Test invalid length valid american card 2"""
        assert credit_card_validator("34") == False
    def test_invalid_length_american_16(self):
        """Test invalid length valid american card 16"""
        assert credit_card_validator("3400000000000091") == False



    """ Invalid Cases """
    def test_empty_imput(self):
        """Test empty imput"""
        assert credit_card_validator() == False
    def test_empty_string(self):
        """Test empty string"""
        assert credit_card_validator("") == False
    def test_unsupported_prefix16(self):
        """Unsuported valid card 16"""
        assert credit_card_validator("1764789618119442") == False
    def test_unsupported_prefix15(self):
        """Unsuported valid card 15"""
        assert credit_card_validator("288645097281526") == False
