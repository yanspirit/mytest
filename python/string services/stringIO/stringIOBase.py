import StringIO
#import cStringIO   more effective

output = StringIO.StringIO()
output.write('First lline.\n')

print >>output, 'Second line'

contents = output.getvalue()

print contents

output.close()