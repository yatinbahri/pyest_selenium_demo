### IMPORTANT if running tests on mac for file test_beam_repo_actions.py - 

1. Please include  # -*- coding: utf-8 -*- in the header
2. Encode the title before assertion Example - page_title.encode('utf-8') == "title"
3. Uncomment code on line 123
4. Uncomment code on line 142




### IMPORTANT if running tests on mac for file test_beam_git_extract.py- 

1. Please include  # -*- coding: utf-8 -*- in the header
2. Encode the title before assertion  Example - page_title.encode('utf-8') == "title"


###To run the test in terminal, navigate to folder where file is saved.

To run all the test file at once -pytest -s -v


To run individual tests 

- pytest test_pytest_demo.py -s -v  # -s will display the print -v will display result

- pytest test_pytest_demo2.py -s -v


### Run tests on different browsers 

1.FireFox - update .Chrome to .gecko.driver and provide the path to gecko driver in Setup method 

2.Safari - update .Chrome to .safari and provide the path to safari driver in Setup method 


