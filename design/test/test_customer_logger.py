from design.customer_logger import CustomerLogger


def test_example():
    logger = CustomerLogger()

    logger.log_customer('1')
    logger.log_customer('2')
    logger.log_customer('4')
    logger.log_customer('2')
    logger.log_customer('5')

    assert logger.get_oldest_customer_for_email() == '1'
    assert logger.get_oldest_customer_for_email() == '4'
    assert logger.get_oldest_customer_for_email() == '5'


def test_empty_logger():
    logger = CustomerLogger()

    logger.log_customer('1')
    logger.log_customer('2')
    logger.log_customer('3')

    assert logger.get_oldest_customer_for_email() == '1'
    assert logger.get_oldest_customer_for_email() == '2'
    assert logger.get_oldest_customer_for_email() == '3'
    assert logger.get_oldest_customer_for_email() == 'N/A'

    logger.log_customer('3')
    logger.log_customer('4')
    logger.log_customer('6')

    assert logger.get_oldest_customer_for_email() == '4'
    assert logger.get_oldest_customer_for_email() == '6'
    assert logger.get_oldest_customer_for_email() == 'N/A'


def test_three_login_in_a_row():
    logger = CustomerLogger()

    logger.log_customer('1')
    logger.log_customer('1')
    logger.log_customer('1')

    assert logger.get_oldest_customer_for_email() == 'N/A'
