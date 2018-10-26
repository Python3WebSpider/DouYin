from retrying import retry


def need_retry(exception):
    return isinstance(exception, RuntimeError)


@retry(stop_max_attempt_number=4, wait_random_min=1000, wait_random_max=3000, retry_on_exception=need_retry)
def run():
    print('Retrying...')
    raise RuntimeError


if __name__ == '__main__':
    run()
