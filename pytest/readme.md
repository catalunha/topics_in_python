catalunha@pop-os:~/apps/topics_in_python/pytest$ poetry add pytest
catalunha@pop-os:~/apps/topics_in_python/pytest$ poetry shell

(topics-in-python-py3.12) catalunha@pop-os:~/apps/topics_in_python/pytest$ pytest test_code_1.py -v
====================================================================== test session starts =======================================================================
platform linux -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0 -- /home/catalunha/apps/topics_in_python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/catalunha/apps/topics_in_python
configfile: pyproject.toml
collected 2 items                                                                                                                                                

test_code_1.py::TestAdd::test_add_positive PASSED                                                                                                          [ 50%]
test_code_1.py::TestAdd::test_add_negative PASSED                                                                                                          [100%]

======================================================================= 2 passed in 0.01s ========================================================================
(topics-in-python-py3.12) catalunha@pop-os:~/apps/topics_in_python/pytest$ 