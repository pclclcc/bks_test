from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device
from snippet_uiautomator import uiautomator
import datetime
import time


_VCB_BANK_APP_TEXT = 'VCB Digibank'
_VCB_FIELD_ID = 'com.VCB:id/frInputField'
_VCB_USERID_LIST = ['1', '2', '3', '4', '5', '6', '7', '8']

_TECHCOMBANK_APP_TEXT = 'Techcombank'
_TECHCOMBANK_LOGIN_TEXT = 'Log in'
# _TECHCOMBANK_USERNAME_FIELD_ID = 'vn.com.techcombank.bb.app:id/edtUsername'
_TECHCOMBANK_USERNAME_TEXT = 'HELLO'
# _TECHCOMBANK_PWD_FIELD_ID = 'vn.com.techcombank.bb.app:id/edtPassword'
_TECHCOMBANK_PWD_TEXT = 'WORLD'

_BIDV_BANK_APP_TEXT = 'SmartBanking'
_BIDV_LOGIN_ID = 'com.vnpay.bidv:id/vCenterLogin'
_BIDV_PHONE_FIELD_ID = 'com.vnpay.bidv:id/wrap_phone'
_BIDV_PHONE_NUMBER_TEXT = '0912345678'
_BIDV_PWD_TEXT = '123456'

# class FindError(Exception):
#     """Exception raised for errors in the input.

#     Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """
#     def __init__(self, value):
#         self.value = value
    
#     def __str__(self):
#       return(f'{self.value} not found!')

class MoblyTest(base_test.BaseTestClass):


  def setup_class(self):
    # Registering android_device controller module declares the test's
    # dependency on Android device hardware. By default, we expect at least one
    # object is created from this.
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    self.dut.services.register(
    uiautomator.ANDROID_SERVICE_NAME,
    uiautomator.UiAutomatorService,)

  # Open VCB Bank App
  def test_open_vcb(self):
    # 回到主畫面
    self.dut.ui.press.home()   
    # 開啟"VCB"App
    self.dut.ui(text=_VCB_BANK_APP_TEXT, desc=_VCB_BANK_APP_TEXT).click.wait()
    # Press Allow button of Permission if needed
    self.press_allow()
    # Input ID 123456789
    self.dut.ui(res=_VCB_FIELD_ID).wait.click()
    time.sleep(2)
    for i in _VCB_USERID_LIST:
        time.sleep(0.5)
        self.dut.adb.shell(['input', 'keyevent', f'KEYCODE_{i}'])
    # Press 'Back' 5 times to Home
    for _ in range(5):
      self.dut.ui.press.back()

  # Open Techcombank App
  def test_open_techcombank(self):
    # 回到主畫面
    self.dut.ui.press.home()   
    # 開啟"Techcombank" App
    self.dut.ui(text=_TECHCOMBANK_APP_TEXT, desc=_TECHCOMBANK_APP_TEXT).click.wait()
    # Press Allow button of Permission if needed
    self.press_allow()
    # Click 'Log in' button
    self.dut.ui(text=_TECHCOMBANK_LOGIN_TEXT).wait.click()
    # Input username
    self.dut.adb.shell(['input', 'text', _TECHCOMBANK_USERNAME_TEXT])
    self.dut.ui.press.enter()
    time.sleep(2)
    # Input password
    self.dut.adb.shell(['input', 'text', _TECHCOMBANK_PWD_TEXT])
    # Press 'Back' 5 times to Home
    for _ in range(5):
        self.dut.ui.press.back()

  # Open BIDV Bank App
  def test_open_bidv(self):
    # 回到主畫面
    self.dut.ui.press.home()   
    # 開啟"BIDV" App
    self.dut.ui(text=_BIDV_BANK_APP_TEXT, desc=_BIDV_BANK_APP_TEXT).click.wait()
    # Press Allow button of Permission if needed
    self.press_allow()
    # Click 'Log in' button
    self.dut.ui(res=_BIDV_LOGIN_ID).wait.exists(datetime.timedelta(seconds=10))
    self.dut.ui(res=_BIDV_LOGIN_ID).click.topleft()
    # Input phone number
    self.dut.ui(res=_BIDV_PHONE_FIELD_ID).wait.click()
    # Input phone number
    self.dut.adb.shell(['input', 'text', _BIDV_PHONE_NUMBER_TEXT])
    time.sleep(1)
    # Input password
    self.dut.ui(res=_BIDV_PHONE_FIELD_ID).bottom(clazz='android.widget.FrameLayout').click.wait()
    self.dut.adb.shell(['input', 'text', _BIDV_PWD_TEXT])
    # Press 'Back' 5 times to Home
    for _ in range(5):
            self.dut.ui.press.back()
 
  #  Press Allow button of Permission if needed
  def press_allow(self):
    allow_button = self.dut.ui(text='Allow')
    if allow_button.wait.exists(datetime.timedelta(seconds=5)):
      allow_button.click.wait()

if __name__ == '__main__':
  test_runner.main()