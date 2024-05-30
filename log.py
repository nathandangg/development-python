import logging

# Create formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Create file handler for foo.bar
file_handler_foo_bar = logging.FileHandler('foo.bar.log')
file_handler_foo_bar.setLevel(logging.INFO)
file_handler_foo_bar.setFormatter(formatter)

# Create file handler for foo
file_handler_foo = logging.FileHandler('foo.log')
file_handler_foo.setLevel(logging.DEBUG)
file_handler_foo.setFormatter(formatter)

# Create logger 'foo' and 'foo.bar'
logger_foo = logging.getLogger('foo')
logger_foo.setLevel(logging.DEBUG)
logger_foo.addHandler(console_handler)
logger_foo.addHandler(file_handler_foo)

logger_foo_bar = logging.getLogger('foo.bar')
logger_foo_bar.setLevel(logging.DEBUG)
logger_foo_bar.addHandler(console_handler)
logger_foo_bar.addHandler(file_handler_foo_bar)

# Test logging
logger_foo.debug('This is a debug message from foo')
logger_foo.info('This is an info message from foo')

logger_foo_bar.debug('This is a debug message from foo.bar')
logger_foo_bar.info('This is an info message from foo.bar')
