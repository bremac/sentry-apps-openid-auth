from distutils.core import setup

setup(name='sentry-apps-openid-auth',
      version='1.0',
      description='Hack to add single-domain Google Apps auth to sentry',
      author='Brendan MacDonell',
      author_email='brendan@macdonell.net',
      license='BSD',
      packages=['sentry_apps_openid_auth'],
      install_requires=[
          'django-openid-auth==0.4',
          'python-openid-patched==2.2.5',
          'sentry==4.8.2',
      ],
      dependency_links=[
          'git+https://github.com/adieu/python-openid.git@03773fb96dff352bbda12538726dc5c46fe0316c#egg=python-openid-patched-2.2.5',
      ]
)
