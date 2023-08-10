from setuptools import setup

setup(
    name="emailsender_rht",
    version="0.1.0",
    description="This package makes it easy to send emails to people.",
    author="Rostel High-Tech",
    author_email="rostelhightech@gmail.com",
    url="https://github.com/rostelhightech",
    packages=["emailsender_rht"],
    install_requires=[
        "smtplib",
        "email",
    ],
    license='MIT',
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS']
)
