import unittest
from unittest import mock


class SFTPResponse:
    def __init__(self, status, content=None, file_name=None):
        self.status = status
        self.content = content
        self.file_name = file_name


class MySFFTPClient:
    succeed_exit_code = 'succeed'
    failure_exit_code = 'failure'

    def read_file(self, remote_file_name) -> SFTPResponse:
        return SFTPResponse(
            status=self.succeed_exit_code,
            content='some analystist info',
            file_name=remote_file_name
        ) if len(remote_file_name) > 4 else SFTPResponse(
            status=self.failure_exit_code)


class ReportBuilder:

    def check_qc(self, file_content):
        return True if len(file_content) >= 10 else False

    def build_report(self, file_content) -> str:
        report_obj = file_content + '. pipeline out'
        return report_obj

    def run_pipeline(self, file_name):
        sftp_resp = MySFFTPClient().read_file(file_name)
        if sftp_resp != MySFFTPClient.succeed_exit_code:
            if self.check_qc(sftp_resp.content):
                with open('tmp/report_file', 'w') as f:
                    f.write(self.build_report(sftp_resp.content))


class CustomTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.report_builder = ReportBuilder()

    def test_check_qc_positive(self):
        file_content = 'aa' * 10
        self.assertTrue(self.report_builder.check_qc(file_content))

    def test_check_qc_negative(self):
        file_content = 'a' * 9
        self.assertFalse(self.report_builder.check_qc(file_content))

    def test_build_report(self):
        file_content = 'Some string'
        actual_report = self.report_builder.build_report(file_content)
        expected_report = file_content + '. Some pipline out'
        self.assertFalse(self.report_builder.check_qc(file_content))
        self.assertEqual(expected_report, actual_report)

    @mock.patch('custom_tests.MySFFTPClient.read_file', return_value=SFTPResponse(
        status=MySFFTPClient.succeed_exit_code,
        content='some analystist info'
    ))
    def test_run_pipeline(self, read_file):
        self.report_builder.run_pipeline('some_file')

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
