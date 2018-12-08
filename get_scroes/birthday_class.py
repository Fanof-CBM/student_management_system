# 以下为底层类


def from_string(data_str):
    def match(*args, **kwargs):
        data = data_str(*args, **kwargs)
        print(data[:])
        return data
    return match


class Data(object):
    # 提供日期对象，可用于用户手动输入生日日期等；

    @from_string
    def data_str(self):
        # 格式化输入年月日
        year = input("year:")
        while len(year) < 4:
            year = '0' + year
        month = input("month:")
        while len(month) < 2:
            month = '0' + month
        day = input("day:")
        while len(month) < 2:
            day = '0' + day
        return year,month,day

    @staticmethod
    def is_data_legal(*args):
        # 检测日期合法性
        import time
        if args:
            year = str(args[0][0])
            month = str(args[0][1])
            day = args[0][2]
            try:
                time.strptime(year,"%Y")
                time.strptime(month,"%m")
                time.strptime(day,"%d")
            except Exception as err:
                print(err)
                return print('illegal time')


# i = Data()
# i.is_data_legal(i.data_str())
