from design.customer_logger import CustomerLogger


def test_customer_logger():
    logger = CustomerLogger()

    logger.log_customer('1')
    logger.log_customer('2')
    logger.log_customer('4')
    logger.log_customer('2')
    logger.log_customer('5')

    assert logger.next_non_returning_customer() == '1'
    assert logger.next_non_returning_customer() == '4'
    assert logger.next_non_returning_customer() == '5'

    logger.log_customer('5')

    assert logger.next_non_returning_customer() == 'N/A'
    assert logger.next_non_returning_customer() == 'N/A'

    logger.log_customer('3')
    logger.log_customer('4')
    logger.log_customer('6')

    assert logger.next_non_returning_customer() == '3'
    assert logger.next_non_returning_customer() == '6'
    assert logger.next_non_returning_customer() == 'N/A'
