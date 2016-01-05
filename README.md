# headlines
Get proper titleization for Python strings.

Python's title() function for __unicode__ strings capitalizes 
inappropriate words, like a, an, for, via, etc. Headlines does not.

# Usage
      >>>import headlines 
      >>>headlines.titleize(u"hey to you")
      u'Hey to You'
      >>>
# Run test suite
Headlines uses py.test for its test suite.

      py.test test_headlines.py
