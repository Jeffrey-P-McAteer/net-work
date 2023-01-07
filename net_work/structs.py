


class NetWork:
  '''
  Represents all the details needed to make remote calls and read remote responses.
  Provides both a syncronous and an asyncronous API.
  '''

  def __init__(self, shared_work_in_directory, shared_work_out_directory=None, work_req_prefix='call_', work_response_prefix='return_'):
    '''
    :param str shared_work_in_directory: Shared network directory where input requests and files will be written
    :param str shared_work_out_directory: Optional, defaults to shared_work_in_directory if unspecified. Directory where completed work will be written.
    :param str work_req_prefix: Prefix to use for input file names
    :param str work_response_prefix: Prefix to use for output file names
    '''
    self.shared_work_in_directory = shared_work_in_directory

    # If unspecified, out directory is the same as in directory.
    if shared_work_out_directory is None:
      self.shared_work_out_directory = shared_work_in_directory
    else:
      self.shared_work_out_directory = shared_work_out_directory


