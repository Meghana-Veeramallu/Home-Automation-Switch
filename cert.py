from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

def create_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

def create_cert(subject_name, issuer_name, issuer_key, subject_key, is_ca=False):
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, subject_name)])
    issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, issuer_name)])
    cert_builder = x509.CertificateBuilder(
    ).subject_name(subject
    ).issuer_name(issuer
    ).public_key(subject_key.public_key()
    ).serial_number(x509.random_serial_number()
    ).not_valid_before(datetime.datetime.utcnow()
    ).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))

    if is_ca:
        cert_builder = cert_builder.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True)
    else:
        cert_builder = cert_builder.add_extension(
            x509.BasicConstraints(ca=False, path_length=None), critical=True)

    cert = cert_builder.sign(private_key=issuer_key, algorithm=hashes.SHA256())
    return cert

def save_key_and_cert(key, cert, key_path, cert_path):
    with open(key_path, "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()))
    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

# Generate CA key & cert
ca_key = create_key()
ca_cert = create_cert("MyCA", "MyCA", ca_key, ca_key, is_ca=True)
save_key_and_cert(ca_key, ca_cert, "ca.key", "ca.crt")

# Generate Server key & cert signed by CA
server_key = create_key()
server_cert = create_cert("localhost", "MyCA", ca_key, server_key)
save_key_and_cert(server_key, server_cert, "server.key", "server.crt")

# Generate Client key & cert signed by CA
client_key = create_key()
client_cert = create_cert("client1", "MyCA", ca_key, client_key)
save_key_and_cert(client_key, client_cert, "client.key", "client.crt")

print("✅ Certificates generated!")
