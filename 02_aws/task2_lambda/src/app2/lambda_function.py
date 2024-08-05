import json
from proj import module3

def lambda_handler(event, context):
    urls = event.get('urls', [])
    valid_count = module3.count_valid_urls(urls)
    invalid_urls = module3.get_invalid_urls(urls)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'valid_count': valid_count,
            'invalid_urls': invalid_urls
        })
    }
