import boto3
import base64

# Use this function in the python shell to encrypt the
# values you will store in the config file
def encrypt(b_plaintext, key_id):
    """Encrypt plaintext with KMS key"""
    kms = boto3.client('kms')
    kms_result = kms.encrypt(
        # Sample key_id format: 'alias/MyAliasName'
        KeyId = key_id, 
        Plaintext = b_plaintext
    )
    ciphertext = base64.b64encode(kms_result['CiphertextBlob'])
    print ciphertext
    return ciphertext