from distutils.core import setup

setup(name='sentry-apps-openid-auth',
      version='1.0.1',
      description='Hack to add single-domain Google Apps auth to sentry',
      author='Brendan MacDonell',
      author_email='brendan@macdonell.net',
      license='BSD',
      packages=['sentry_apps_openid_auth'],
      install_requires=[
          'python-openid==2.2.5-apps',
          'django-openid-auth==0.4',
          'sentry',
      ],
      dependency_links=[
          'git+https://github.com/bremac/python-openid.git@8744683137441cbaefecf6de0015242017df0ba1#egg=python-openid-2.2.5-apps',
      ]
)
