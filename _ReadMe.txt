####For interpreter...
####From Terminal
pip install -U selenium
pip install –U pytest
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest
pip install allure-pytest-commons


####For HTML report
pytest -v Tests\Test_Cases\  page name .py extensions  --html=./hubSpot.html


####For Making allure results and generate report
1- pytest -v -s Tests\testcase OR test suite /page name .py extension --alluredir=allure-results
2- allure generate allure-results --clean & allure open

####For add in a specific folder --alluredir=Allure/Results/
allure generate Allure/Results/ -o Allure/Reports --clean & allure open Allure/Reports


####For run test suit in suite folder..
must use pytest.mark."Description" before suite method
pytest -v -s -m Description in console


####For checking specific features ..make sure the    '@allure.feature("Feature name")'  is added before the test case
pytest -v -s Tests\Test_Suite\Test_Suites.py --allure-features "Feature name"


####ONLy USE####
Only TestCases/TestSuites Folders in Tests
Dont use Main and libraries folder
Dont delete any __init__.py from any folders...
if dont have knowledge of confest page dont use multibrowser or parallel execution

for making the final allure report make sure your envinment files in in the allure result folder.

####Compulsory for making test case must have
Allure Feature
Title
Decription


####For Flow and making tests
1****####Data
Add data into TestData Folder...
if added so load the file in the TestData __init__.py
add more folder or not its upto you.
but difference files for ids and data...

2****####Page
If new page..Add Page in to Pages Folder and Add the interactions ID in it From Test Data 'specific id page you using'
and make the intereaction methods alone by calling from corepage..
like method is:-            EnterNameinform(,username,allure step,allure screenshotname)
add click from corepage:-           EnterText(pass the ids,data,allure step,allure screenshotname)
now u pass only ids...and Data would add in test cases page..

3****####TestsCases
In TEstCases
You can add page with the name of 'test_' then page name you like
and then make differenct senarios by using the method of pages and logic from corepage too iif needed
and add data and its upto you how you can make senarios,,,
but make sure....
in senarios you can add 'data', 'allurestep' and 'allurescreenshot name' in every methods you useing from core or Pages

4****####TestSenario
in senario just add test class names to make senarios,,


#####BASIC FLOW
Jason files-->  (laod to __init__.py in testDAta folder if new)
Pages-->        (id load only) rest of things would return same
TestCases-->    make differenct senarios and run from test case
OR
TesttSuites-->  call Testcase classes for calling senarios


**************#THANKYOU#****************




        self.dashboard.get_upload_file_with_path("C:\\Users\\Pk Teams\\Downloads\\Draft Quotation Export18209.xlsx","Uplaod file")


    @allure.suite("Create Quotation")
    @allure.feature("Create Quotation")
    @allure.title('Create Quotation')
    @allure.description('Making the quotation from the dashboard and entering the right data to check the flow')
    def test_Create_Quotation2(self):
        self.lp1 = LoginPage(self.driver)
        self.lp1.get_url(ReadConfig_URL.SET_ADMIN_URL(), "URL Entered")
        self.lp1.enter_username(ReadConfig_LOGIN.SET_LOGIN_EMAIL(), "Admin Username")
        self.lp1.enter_password(ReadConfig_LOGIN.SET_LOGIN_PASSWORD(), "Admin password")
        self.lp1.enter_click("Login Button Click")


        self.lp1.is_title("Wholesale (Test Server) | Dashboard", "Title url",)
        self.lp1.is_wait_sleep(5)
        self.dashboard = DashboardPage(self.driver)
        self.dashboard.Create_Quotation_btn( "create quotation from dashboard")
        self.dashboard.is_tab_switch(1,"create quotation window")
        self.lp1.is_wait_sleep(5)

        # self.driver.find_element_by_css_selector("div.col-lg-12.col-md-12.text-uppercase.fontbold >div>a>button").click()
        # self.driver.find_element_by_css_selector("#uploadDocument > div > div > div.row.justify-content-end > a").click()
        # self.lp1.is_wait_sleep(5)
        #
        # self.lp1.get_upload_file_with_path("C:\\Users\\Pk Teams\\Downloads\\Draft Quotation Export18209.xlsx","Uplaod file")


        self.quotationpage = QuotationPage(self.driver)
        self.quotationpage.Bill_To_dropdown(self.customername_Data,"click to billto")
        self.quotationpage.is_wait_sleep(2)
        # self.quotationpage.Add_Product_By_ReferenceNo("DC2","Enter product")
        # self.quotationpage.is_wait_sleep(2)
        # self.quotationpage.Add_Product_By_Btn("DC9","addproduct")
        #
        #

 newman.run({
        collection: 'your collection path ',
        environment: 'env file path',
        reporters: ['html', 'cli', 'junit', 'json', 'allure'],
        reporter: {
            html: {
                export: '/your/path'
            },
            junit: {
                export: '/your/path'
            },
            json: {
                export: '/your/path'
            },
            allure: {
                export: 'results/allure'
            }
        },
        color: true
    }
npx allure generate results/allure --clean -o results/allure-htmlReport
npx allure open results/allure-htmlReport
