# locators.py
from selenium.webdriver.common.by import By

############## BASE LOCATORS ##############
class BasePageLocators:
    TITLE = 'MIPR Tracking Tool'
    SEARCH_BOX = (By.XPATH, '//input[@name="q"]')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search-icon')
    SEARCH_TERM = 'DJP'
    SEARCH_RESULTS = (By.XPATH, '//span[@class="dataview-header-title-headline"]')
    ALL_ITEMS = (By.LINK_TEXT, 'All Items')
    ADMIN_PORTAL = (By.XPATH, '//li[@class="icon-link admin-icon-link"]')
    ACCOUNT_DROPDOWN = (By.XPATH, '//li[@class="icon-link logout-dropdown"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div/ul/li[7]/div/ul/li[2]/a')
    PATCH_NOTES = (By.XPATH, '//li[@class="icon-link notes-icon-link"]')
    PATCH_NOTES_BODY = (By.XPATH, '//div[@class="patchnotes-container"]')

    # Dropdown Locators #
    DROPDOWN_MENU = (By.XPATH, '//h1[@class="site-title"]')
    DROPDOWN_LIST = (By.XPATH, '/html/body/div[3]/ul')

    MODAL_HEADER = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/header/h3')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@class="modal-close"]')

   

class LoginPageLocators:
    URL = ''
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')

class HomePageLocators:
    URL = 'financial-management'
    CREATEMIPRBUTTON = (By.XPATH, '//button[@class="btn btn-primary dataview-create-record"]')

    # DataView Icons #
    EXPORTREPORT = (By.XPATH, '//button[@class="btn dataview-icon-btn export-button"]')
    COLUMNSICON = (By.XPATH, '//button[@class="btn btn-info dataview-icon-btn"]')
    COLUMNSLIST = (By.XPATH, '//ul[@class="column-list"]')
    COLUMNS = ["7600B", "Acceptance Type", 'ACRN:Labor', 'ACRN:Materials', 'ACRN:ODC',
               'ACRN:Travel', 'Amendment', 'Archived', 'Assigned To', 'Contract $', 'CSDC $', 
                'CSDC Return Fee $', 'CSDC Waived by Director', 'DAI Category', 'Date Approved in DAI',
                 'Date Created', 'Email Received (from Customer)', 'F_ID', 'FY', 'Latest Status',
                  'MIPR Number', 'MOD #', 'Modified', 'Passed Initial Review', 'Phase', 'PO Award Date',
                   'POP', 'POP End', 'POP Start', 'Primary COR', 'Priority', 'Req Agency POA', 'RMS (Last 4)',
                    'RMS ID Number', 'Service', 'SLIN:Labor', 'SLIN:Materials', 'SLIN:ODC', 'SLIN:Travel',
                     'Status Date', 'Urgent', 'Zero Cost MIPR' ]
    STATUS_CHART = (By.XPATH, '//button[@class="btn dataview-icon-btn"]')
    STATUS_CHART_TITLE = (By.XPATH, '//h2[@class="modal-title"]')
    PRIORITY_LEGEND = (By.XPATH, '//button[@class="btn btn-danger dataview-icon-btn"]')

    # PHASE CHECKBOXES #
    CHECKEDSTATUS = 'horizontal-phase-menu-list-item active'
    UNCHECKEDSTATUS = 'horizontal-phase-menu-list-item '

    LOGGING = '//input[@id="checkbox-Logging"]'
    LOGGINGTOTAL = '#root > div > main > div > div:nth-child(2) > div.dataview-header > div > ul > li:nth-child(2) > span > span.horizontal-phase-menu-list-item-label-sub'
    
    EVALUATING = '//input[@id="checkbox-Evaluating"]'
    EVALUATINGTOTAL = '#root > div > main > div > div:nth-child(2) > div.dataview-header > div > ul > li:nth-child(3) > span > span.horizontal-phase-menu-list-item-label-sub'
   
    PROCESSING = '//input[@id="checkbox-Processing"]'
    PROCESSINGTOTAL = '#root > div > main > div > div:nth-child(2) > div.dataview-header > div > ul > li:nth-child(4) > span > span.horizontal-phase-menu-list-item-label-sub'
    
    OBLIGATING = '//input[@id="checkbox-Obligating"]'
    OBLIGATINGTOTAL = '#root > div > main > div > div:nth-child(2) > div.dataview-header > div > ul > li:nth-child(5) > span > span.horizontal-phase-menu-list-item-label-sub'
    
    COMPLETED = '//input[@id="checkbox-Completed"]'
    COMPLETEDTOTAL = '#root > div > main > div > div:nth-child(2) > div.dataview-header > div > ul > li:nth-child(6) > span > span.horizontal-phase-menu-list-item-label-sub'
    
    FOUNDRECORDSTOTAL = '#root > div > main > div > div:nth-child(2) > div.box.dataview-box > div.dataview-pagination > div.dataview-pagination--left'

    

class BaseModalLocators:
    MODALTITLE = (By.XPATH, '//h2[@class="modal-title"]')

############## DROPDOWN LOCATORS ##############
class UserWorkFlowLocators:
    URL = 'workflow'

class AllItemsLast30Locators:
    URL = 'all-items-last-30'

class AllItemsFYLocators:
    URL = 'all-items-fy'

class BaselinedCOMODRequiredLocators:
    URL = 'co-mod-required'
    DROPDOWN_LINKTEXT = 'CO MOD Required'
    TITLE = '//*[@id="root"]/div/main/div/div[1]/div[1]/h3/span[1]'
    TITLE_VALUE = 'CO MOD Required'
    COLUMNS_ICON = (By.XPATH, '//span[@class="dataview-header-title-headline"]')
    COLUMNS_MODAL_TITLE = (By.XPATH, '//*[@id="root"]/div/main/div/div[1]/div[2]/div/div/div/header/h2')
    COLUMNS_LIST = (By.XPATH, '//ul[@class="column-list"]')
    COLUMNS = ['Acceptance Type', 'Amendment', 'Assigned to', 
               'Contract $', 'FY', 'Latest Status', 'MIPR Number',
               'MOD #', 'Phase', 'PO Award', 'RMS ID Number', 
               'Status Date', 'Zero Cost MIPR']

class RmsIdNumberLookupLocators:
    URL = 'rms-id-number-lookup'
    TITLE = '//*[@id="root"]/div/main/section/section/div[1]/div[1]/h3/span'
    TITLE_VALUE = 'RMS ID Number Lookup'

############## MIPR MODAL LOCATORS ##############
class MiprModalLocators:
    MIPRNUMBERNAME = (By.ID, 'mipr_number')
    VALIDATEBUTTON = (By.XPATH, '//button[@class="btn btn-primary btn-interior"]')
    AMENDMENTSELECT = (By.XPATH, '//*[@id="react-select-2-input"]')
    CURRENTFY = (By.ID, 'current_fy')
    RMSID = (By.XPATH, '//*[@id="react-select-3-input"]')
    # EMAILRECEIVEDDATE = (By.XPATH, '//input[@id="email_received"]')
    EMAILRECEIVEDDATE = (By.XPATH, '//input[@id="email_received"]')
    PRIMARYCOR = (By.XPATH, '//select[@id="PCOR"]')
    ACORNAME = (By.XPATH, '//input[@id="acor_name"]')
    CONTRACTAMOUNT = (By.XPATH, '//input[@id="TATAmt"]')
    CSDCAMOUNT = (By.XPATH, '//input[@id="CSDCAmt"]')
    SERVICEBRANCH = (By.XPATH, '//select[@id="service"]')
    PRIORITY = (By.XPATH, '//select[@id="priority"]')
    DETERMINATION = (By.XPATH, '//select[@id="determination"]')
    CREATEBUTTON = (By.XPATH, '//input[@class="btn blue"]')



############## ADMIN PORTAL LOCATORS ##############

class AdminPortalPageLocators:
    URL = 'admin-portal/'
    MIPRNUMBERS = (By.LINK_TEXT, 'MIPR Numbers')

class AdminMiprNumberLocators:
    URL = str(AdminPortalPageLocators.URL)+ 'mipr-admin'
    PAGE_TITLE = '//*[@id="root"]/div/main/div/div/div[3]/div/h2'
    TITLE_VALUE = 'MIPR Numbers'
    LOADALLMIPRSBUTTON = (By.XPATH, '//button[@class="btn btn-success load-all-miprs"]')
    FINDMIPRBYNAME = (By.XPATH, '//input[@name="query"]')
    MIPRNAMEFINDBUTTON = (By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[1]/form[1]/p[2]/input[2]')
    FINDMIPRBYUSER = (By.XPATH, '//*[@name="assign"]')
    USERFINDBUTTON = (By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[1]/form[2]/p[2]/input')
    BULKEDITDROPDOWN = (By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[3]/div[2]/form/p/select')
    BULKEDITNEXTBUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/div[2]/form/p/input')
    BULKEDITVALUE = (By.XPATH, '//select[@id="bulk-edit-value"]')
    BULKEDITSAVEBUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/div[2]/form/div/input')

class AdminUsersLocators:
    URL = str(AdminPortalPageLocators.URL)+ 'add-user'

class AdminRMSLocators:
    URL = str(AdminPortalPageLocators.URL)+ 'rms-admin'
    PAGE_TITLE = '//*[@id="root"]/div/main/div/div/div[3]/div/div/h2'
    TITLE_VALUE = 'RMS ID Numbers'
    ADDRMSBUTTON = (By.XPATH, '//button[@class="btn"]')
    RMSSEARCH = (By.ID, 'search-input')
    EDIT = (By.LINK_TEXT, 'Edit')
    DELETE = (By.CLASS_NAME, 'btn btn-danger')
    CONFIRMDELETE = (By.CLASS_NAME, 'btn btn-success')
    # Modal Locators Below #
    MODALRMSTITLE = (By.XPATH, '//h2[@class="modal-title"]')
    MODALRMSIDNUMBER = (By.ID, 'Ord_Name')
    MODALRMSCORSELECT = (By.ID, 'cor')
    MODALRMSPRIORITYSELECT = (By.ID, 'priority')
    MODALRMSACTIVESELECT = (By.ID, 'active')
    MODALRMSCREATEBUTTON = (By.XPATH, '//input[@type="submit"]')


class AdminMiprLifeCycleLocators:
    URL = str(AdminPortalPageLocators.URL)+ 'mipr-life-cycle'

class AdminRAPOAsLocators:
    URL = str(AdminPortalPageLocators.URL + 'rapoas-admin')

class AdminStatusLocators:
    URL = str(AdminPortalPageLocators.URL + 'status-admin')

class AdminMiprHistoryLocators:
    URL = str(AdminPortalPageLocators.URL + 'mipr-history')

class AdminRolesLocators:
    URL = str(AdminPortalPageLocators.URL + 'admin/roles')

class AdminTabsLocators:
    URL = str(AdminPortalPageLocators.URL + 'tab-admin')

class AdminStatusUpdateLocators:
    URL = str(AdminPortalPageLocators.URL + 'update-mipr-status')

class AdminMiprDataReportLocators:
    URL = str(AdminPortalPageLocators.URL + 'mipr-data-report')

class AdminModulesLocators:
    URL = str(AdminPortalPageLocators.URL + 'admin/modules')