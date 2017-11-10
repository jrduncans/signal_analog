"""This module generated by the `st` transpiler version 0.10.1.

For more information about the purpose of the `st` transpiler check out
the source here:
  https://bitbucket.nike.com/projects/NIK/repos/***REMOVED***/browse

Please report any bugs found to #plus-platform in the NDe Slack or by
e-mail to ***REMOVED***
"""
from six import string_types
class Function(object):
    def __init__(self, name):
        """Base SignalFlow stream function class."""
        if not name:
            raise Exception("Name cannot be None.")
        self.name = name
        self.args = []
        self.call_stack = []
    def __str__(self):
        str_args = ",".join(map(str, filter(lambda x: x.arg, self.args)))
        if not self.call_stack:
            str_calls = ""
        else:
            str_calls = "." + ".".join(map(str, self.call_stack))
        return "%(name)s(%(args)s)%(fn_calls)s" % {"name": self.name, "args": str_args, "fn_calls": str_calls}
    def bottom(self, by=None, over=None):
        """Get the bottom values in the stream.bottom(count=None, percentage=None, by=None)Returns reference to the input  object."""
        self.call_stack.append(Bottom(by=by, over=over))
        return self
    def count(self, by=None, over=None):
        """Counts the number of inputs that have data.count(by=None)count(over=None)Returns reference to the input  object."""
        self.call_stack.append(Count(by=by, over=over))
        return self
    def delta(self, by=None, over=None):
        """Calculates the difference between the current value and the previous value for each time interval. Delta operates independently on each time series.delta()Returns reference to the input  object."""
        self.call_stack.append(Delta(by=by, over=over))
        return self
    def mean(self, by=None, over=None):
        """Find the mean on a stream.mean(by=None)mean(over=None)Returns reference to the input  object."""
        self.call_stack.append(Mean(by=by, over=over))
        return self
    def mean_plus_stddev(self, by=None, over=None):
        """Calculates the mean + n standard deviationsmean_plus_stddev(stddevs=1, by=None)mean_plus_stddev(stddevs=1, over=None)Returns reference to the input  object."""
        self.call_stack.append(Mean_plus_stddev(by=by, over=over))
        return self
    def median(self, by=None, over=None):
        """Find the median on a stream.median(by=None)median(over=None)Returns reference to the input  object."""
        self.call_stack.append(Median(by=by, over=over))
        return self
    def min(self, by=None, over=None):
        """Find the minimum value on a stream.min(by=None)min(over=None)Returns reference to the input  object."""
        self.call_stack.append(Min(by=by, over=over))
        return self
    def max(self, by=None, over=None):
        """Find the maximum value on a stream.max(by=None)max(over=None)Returns reference to the input  object."""
        self.call_stack.append(Max(by=by, over=over))
        return self
    def percentile(self, by=None, over=None):
        """Calculates the n-th percentile of inputs in the stream.percentile(pct, by=None)percentile(pct, over=None)Returns reference to the input  object."""
        self.call_stack.append(Percentile(by=by, over=over))
        return self
    def random(self, by=None, over=None):
        """Get random values in the stream by count or percentage.random(count=None, percentage=None, by=None)Returns reference to the input  object."""
        self.call_stack.append(Random(by=by, over=over))
        return self
    def sample_stddev(self, by=None, over=None):
        """Calculates the sample standard deviation of inputs in the stream. This is less biased than stddev when you have a smaller population size.sample_stddev(by=None)sample_stddev(over=None)Returns reference to the input  object."""
        self.call_stack.append(Sample_stddev(by=by, over=over))
        return self
    def sample_variance(self, by=None, over=None):
        """Calculates the sample variance of inputs in the stream. This is less biased than variance when you have a small sample sizesample_variance(by=None)sample_variance(over=None)Returns reference to the input  object."""
        self.call_stack.append(Sample_variance(by=by, over=over))
        return self
    def size(self, by=None, over=None):
        """Counts the number of inputs in the stream.size(by=None)size(over=None)Returns reference to the input  object."""
        self.call_stack.append(Size(by=by, over=over))
        return self
    def stddev(self, by=None, over=None):
        """Calculates the standard deviation of inputs in the stream.stddev(by=None)stddev(over=None)Returns reference to the input  object."""
        self.call_stack.append(Stddev(by=by, over=over))
        return self
    def sum(self, by=None, over=None):
        """Find the sum on a stream.sum(by=None)sum(over=None)Returns reference to the input  object."""
        self.call_stack.append(Sum(by=by, over=over))
        return self
    def top(self, by=None, over=None):
        """Get the top values in the stream.top(count=None, percentage=None, by=None)Returns reference to the input  object."""
        self.call_stack.append(Top(by=by, over=over))
        return self
    def variance(self, by=None, over=None):
        """Calculates the variance of inputs in the stream.variance(by=None)variance(over=None)Returns reference to the input  object."""
        self.call_stack.append(Variance(by=by, over=over))
        return self
    def integrate(self, by=None, over=None):
        """Multiplies the values of each input time series by the resolution (in seconds) of the computation. Integrate is most useful in SignalFx for gauge metrics.integrate()Returns reference to the input  object."""
        self.call_stack.append(Integrate(by=by, over=over))
        return self
    def map(self, by=None, over=None):
        """Apply a lambda function to a stream.map(mapfn)Returns reference to the input  object."""
        self.call_stack.append(Map(by=by, over=over))
        return self
    def publish(self, by=None, over=None):
        """Publish the output of a stream so that it is visible outside of a computation.publish(label=None)Returns reference to the input  object."""
        self.call_stack.append(Publish(by=by, over=over))
        return self
    def timeshift(self, by=None, over=None):
        """Timeshift the datapoints for a stream, offset by a specified time period e.g. 1 week (1w), to enable comparison of time series with its own past behavior.timeshift(offset)Returns reference to the input stream object."""
        self.call_stack.append(Timeshift(by=by, over=over))
        return self
    def ewma(self, alpha):
        """Calculates the exponentially weighted moving average of the stream.
ewma(alpha)Returns a new  object."""
        self.call_stack.append(Ewma(alpha))
        return self
    def abs(self):
        """Apply absolute value to data in the stream.abs()Returns reference to the input  object."""
        self.call_stack.append(Abs())
        return self
    def ceil(self):
        """Apply the ceil() function to data in the stream.ceil()Returns reference to the input  object."""
        self.call_stack.append(Ceil())
        return self
    def floor(self):
        """Apply floor() to data in the stream.floor()Returns reference to the input  object."""
        self.call_stack.append(Floor())
        return self
    def log(self):
        """Apply the natural log function to data in the stream.log()Returns reference to the input  object."""
        self.call_stack.append(Log())
        return self
    def log10(self):
        """Apply the logarithm(base 10) function to data in the stream.log10()Returns reference to the input  object."""
        self.call_stack.append(Log10())
        return self
    def pow(self, exponent):
        """ - return (stream data)"""
        self.call_stack.append(Pow(exponent))
        return self
    def pow(self, base=None):
        """ - return base"""
        self.call_stack.append(Pow(base=base))
        return self
    def scale(self, multiplier):
        """Scale data in the stream by a multiplierscale(multiplier)Returns reference to the input  object."""
        self.call_stack.append(Scale(multiplier))
        return self
    def sqrt(self):
        """Apply a square root to data in the stream.sqrt()Returns reference to the input  object."""
        self.call_stack.append(Sqrt())
        return self
    def above(self, limit, inclusive=None, clamp=None):
        """Only pass through data in the stream that is above a particular value, or clamp data above a value to that value.
above(limit, inclusive=False, clamp=False)Returns reference to the input  object."""
        self.call_stack.append(Above(limit, inclusive=inclusive, clamp=clamp))
        return self
    def below(self, limit, inclusive=None, clamp=None):
        """Only pass through data in the stream that is below a particular value, or clamp data below a value to that value.
below(limit, inclusive=False, clamp=False)Returns reference to the input  object."""
        self.call_stack.append(Below(limit, inclusive=inclusive, clamp=clamp))
        return self
    def between(self, low_limit, high_limit, low_inclusive=None, high_inclusive=None, clamp=None):
        """Only pass through data in the stream that is between two particular values or replace data that is not between two particular values with the limit that they are closest to.
between(low_limit, high_limit, low_inclusive=False, high_inclusive=False, clamp=False)Returns reference to the input  object."""
        self.call_stack.append(Between(low_limit, high_limit, low_inclusive=low_inclusive, high_inclusive=high_inclusive, clamp=clamp))
        return self
    def equals(self, value, replacement=None):
        """Only pass through data in the stream that is equal to a particular value or replace data that is not equal to a particular value with another value
equals(value, replacement=None)Returns reference to the input  object."""
        self.call_stack.append(Equals(value, replacement=replacement))
        return self
    def not_between(self, low_limit, high_limit, low_inclusive=None, high_inclusive=None):
        """Only pass through data in the stream that is not between two particular values
not_between(low_limit, high_limit, low_inclusive=False, high_inclusive=False)Returns reference to the input  object."""
        self.call_stack.append(Not_between(low_limit, high_limit, low_inclusive=low_inclusive, high_inclusive=high_inclusive))
        return self
    def not_equals(self, value, replacement=None):
        """Only pass through data in the stream that is not equal to a particular value or replace data that is equal to a particular value with another value
not_equals(value, replacement=None)Returns reference to the input  object."""
        self.call_stack.append(Not_equals(value, replacement=replacement))
        return self
    def promote(self, property):
        """Promotes a metadata property to a dimension.promote(property), promote([property, ...]), promote(by=None), promote(property, ...)"""
        self.call_stack.append(Promote(property))
        return self
class StreamMethod(object):
    def __init__(self, name):
        """Base SignalFlow stream method class."""
        if not name:
            raise Exception("Name cannot be None.")
        self.name = name
        self.args = []
    def __str__(self):
        str_args = ",".join(map(str, filter(lambda x: x.arg, self.args)))
        return "%(name)s(%(args)s)" % {"name": self.name, "args": str_args}
class StrArg(object):
    def __init__(self, arg):
        if not arg:
            raise Exception("Arg cannot be None.")
        self.arg = arg
    def __str__(self):
        return "\"" + str(self.arg) + "\""
class KWArg(object):
    def __init__(self, keyword, arg):
        if not keyword:
            raise Exception("Keyword cannot be None.")
        self.keyword = keyword
        self.arg = arg
    def __str__(self):
        str_arg = self.arg
        if isinstance(self.arg, string_types):
            str_arg = "\"" + self.arg + "\""
        return "%s=%s" % (self.keyword, str_arg)
class VarStrArg(object):
    def __init__(self, args):
        self.arg = args
    def __str__(self):
        return ",".join(map(lambda x: str(StrArg(x)), self.arg))
class Data(Function):
    def __init__(self, metric, filter=None, rollup=None, extrapolation=None, maxExtrapolations=None):
        """The data() function is used to create a stream:data(metric, filter=None, rollup=None, extrapolation='null', maxExtrapolations=100)"""
        super(Data, self).__init__("data")
        self.args = [StrArg(metric), KWArg("filter", filter), KWArg("rollup", rollup), KWArg("extrapolation", extrapolation), KWArg("maxExtrapolations", maxExtrapolations)]
class Filter(Function):
    def __init__(self, parameter_name, query, *args):
        """Creates a _filter_ object."""
        super(Filter, self).__init__("filter")
        self.args = [StrArg(parameter_name), StrArg(query), VarStrArg(args)]
class Const(Function):
    def __init__(self, value, key, timeseries):
        """The const() function is used to create a stream of constant-value timeseries.const(value=None, key=None, timeseries=None):The simplest usage of the const() function is to generate a single timeseries with no additional dimensions by simply providing a value.You can also specify additional dimensions with the key parameter when generating a single timeseries.The const() function can be used to generate multiple timeseries in its generated output stream. This is useful to define distinct static thresholds for various dimension values. To do this, each output timeseries is specified in the timeseries list parameter as a dictionary with a key and a value."""
        super(Const, self).__init__("const")
        self.args = [StrArg(value), StrArg(key), StrArg(timeseries)]
class Graphite(Function):
    def __init__(self, metric, rollup=None, extrapolation=None, maxExtrapolations=None, **kwargs):
        """The graphite() function is used to create a stream interpreting the metric query as a series of period separated dimensions. This method is useful for querying metrics created by graphite.graphite(metric, rollup=None, extrapolation='null', maxExtrapolations=100, **kwargs)Returns a  object with synthesized dimensions. When the graphite() function is used the metric name is split into several distinct nodes. E.g. api.login.count would get split into three nodes: 'api', 'login', and 'count'. By default each node is named 'nodeN' where N is the zero-index position of the node. E.g. api.login.count would be dimensionalized as node0=api, node1=login, and node2=count. The keyword arguments to the graphite() function can be used to customize the name these nodes have. E.g. passing serverType=0, apiType=1 as keyword arguments, would cause api.login.count to be dimensionalized as serverType=api, apiType=login, and node3=count. These synthesized dimensions can be used in group bys later and will affect the dimensions on the output of the stream."""
        super(Graphite, self).__init__("graphite")
        self.args = [StrArg(metric), KWArg("rollup", rollup), KWArg("extrapolation", extrapolation), KWArg("maxExtrapolations", maxExtrapolations), StrArg("foo")]
class Newrelic(Function):
    def __init__(self, metric, filter=None, rollup=None, extrapolation=None, maxExtrapolations=None, **kwargs):
        """The newrelic() function is used to create a stream interpreting the metric query as a series of slash separated dimensions. This method is useful for querying metrics created by New Relic.newrelic(metric, filter=None, rollup=None, extrapolation='null', maxExtrapolations=100, **kwargs)Returns a  object with synthesized dimensions. When the newrelic() function is used the metric name is split into several distinct nodes. E.g. HttpDispatcher/average_response_time/1273567 would get split into three nodes: 'HttpDispatcher', 'average_response_time', and '1273567'. By default each node is mapped to a dimension name 'nodeN' where N is the zero-index position of the node. E.g. HttpDispatcher/average_response_time/1273567 would be node0=HttpDispatcher, node1=average_response_time, and node2=1273567. The keyword arguments to the newrelic() function can be used to customize the name these nodes have. E.g. passing source=0, applicationId=2 as keyword arguments, would cause HttpDispatcher/average_response_time/1273567 to be dimensionalized as source=HttpDispatcher, node1=average_response_time, and applicationId=1273567. These synthesized dimensions can be used in group bys later and will affect the dimensions on the output of the stream."""
        super(Newrelic, self).__init__("newrelic")
        self.args = [StrArg(metric), KWArg("filter", filter), KWArg("rollup", rollup), KWArg("extrapolation", extrapolation), KWArg("maxExtrapolations", maxExtrapolations), StrArg("foo")]
class Union(Function):
    def __init__(self):
        """The union function merges multiple time series streams into a single time
series stream.The union function accepts a variable number of parameters, each of which must be a time series stream. The streams must all be aggregated similarly (i.e., not aggregated at all, or aggregated by the same property names). At least one stream must be specified, but the function has no effect if only one one argument is specified.The return value is a merged time series stream that contains the time series from all parameters.The union function can throw the following errors:The union function may be used for any computation that can be derived from partial results over subsets of the population. Such computations include max, min, sum, count, top and bottom. (See the Examples section below.) However, note that union is only truly required for top and bottom, since the others may be solved alternatively. For example, by directly invoking the max and min functions over the partially aggregated streams.Note that union cannot be used to naively derive the global mean because the global mean is not simply the mean of the subset means. However, computing the global mean is simple.Finally, note that some computations cannot be derived from partial results and therefore cannot be computed using the union function.SignalFlow computations have a limit on the maximum number of time series that can be processed in a stream. (This limit is 5000 time series per stream, unless your organization has a different limit configured.) The merged stream from the union also obeys this limit. If the total number of time series across all arguments exceeds the limit, the merged stream is filled to capacity in order of the specified arguments.If multiple time series with the same identity exist in different arguments to the union function, only the first instance of the time series (again, defined by order of parameters) is included in the union.For example, the following program will not work as might be expected.If the two regions both have common instance types, only the corresponding instances from the "east" region will be included. Aggregating by the region in addition to the instance type will solve the problem by ensuring that the identities of the time series are unique.The union function may be used to effectively process more time series than the stream size limit. This may may be accomplished by:For example, to find the top 10 loaded instances across an environment:"""
        super(Union, self).__init__("union")
        self.args = []
class Detect(Function):
    def __init__(self, on, off=None, mode=None):
        """Creates a  object.A  object is used to create events when a  condition is met and when it clears. These events can be used to notify people of when the conditions within the detect block are met. In order to actually publish the events the  must be invokeddetect(on, off=None, mode="paired")Returns reference to a  stream.The examples above show simple scenarios in which you apply a single static threshold to all the timeseries of the input stream. In more complex scenarios or infrastructures, it is often needed to have distinct thresholds for different services, or based on some other differentiating dimension.Instead of creating multiple detectors, or having multiple detect()s in the same program, you can use the 's function ability to generate constant-value timeseries with user-defined dimensions and rely on timeseries correlation to match your input timeseries to those thresholds.You can use the  to access a collection of SignalFlow functions, each of which captures a common analytical pattern used in alerting. Most of these functions can be also accessed as  in the SignalFx web UI, such as Stopped Reporting or Sudden Change."""
        super(Detect, self).__init__("detect")
        self.args = [StrArg(on), KWArg("off", off), KWArg("mode", mode)]
class When(Function):
    def __init__(self, predicate, lasting=None, at_least=None):
        """Creates a  object for use in  functions. The  object is a generator of boolean values, depending on whether or not the predicate hold true or not when evaluated. The lasting and at_least parameters can be used to control how long and how often the predicate must be true for the  object to return True when evaluated.when(predicate, lasting=None, at_least=1.0)when(predicate, lasting=None)Returns a  object."""
        super(When, self).__init__("when")
        self.args = [StrArg(predicate), KWArg("lasting", lasting), KWArg("at_least", at_least)]
class Lasting(Function):
    def __init__(self, lasting=None, at_least=None):
        """Convenience wrapper for holding both the lasting and optionally the at_least parameter to pass to a  function.lasting(lasting=None, at_least=1.0)Returns a  object."""
        super(Lasting, self).__init__("lasting")
        self.args = [KWArg("lasting", lasting), KWArg("at_least", at_least)]
class Bottom(StreamMethod):
    def __init__(self, by=None, over=None):
        """Get the bottom values in the stream.bottom(count=None, percentage=None, by=None)Returns reference to the input  object."""
        super(Bottom, self).__init__("bottom")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Count(StreamMethod):
    def __init__(self, by=None, over=None):
        """Counts the number of inputs that have data.count(by=None)count(over=None)Returns reference to the input  object."""
        super(Count, self).__init__("count")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Delta(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the difference between the current value and the previous value for each time interval. Delta operates independently on each time series.delta()Returns reference to the input  object."""
        super(Delta, self).__init__("delta")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Mean(StreamMethod):
    def __init__(self, by=None, over=None):
        """Find the mean on a stream.mean(by=None)mean(over=None)Returns reference to the input  object."""
        super(Mean, self).__init__("mean")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Mean_plus_stddev(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the mean + n standard deviationsmean_plus_stddev(stddevs=1, by=None)mean_plus_stddev(stddevs=1, over=None)Returns reference to the input  object."""
        super(Mean_plus_stddev, self).__init__("mean_plus_stddev")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Median(StreamMethod):
    def __init__(self, by=None, over=None):
        """Find the median on a stream.median(by=None)median(over=None)Returns reference to the input  object."""
        super(Median, self).__init__("median")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Min(StreamMethod):
    def __init__(self, by=None, over=None):
        """Find the minimum value on a stream.min(by=None)min(over=None)Returns reference to the input  object."""
        super(Min, self).__init__("min")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Max(StreamMethod):
    def __init__(self, by=None, over=None):
        """Find the maximum value on a stream.max(by=None)max(over=None)Returns reference to the input  object."""
        super(Max, self).__init__("max")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Percentile(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the n-th percentile of inputs in the stream.percentile(pct, by=None)percentile(pct, over=None)Returns reference to the input  object."""
        super(Percentile, self).__init__("percentile")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Random(StreamMethod):
    def __init__(self, by=None, over=None):
        """Get random values in the stream by count or percentage.random(count=None, percentage=None, by=None)Returns reference to the input  object."""
        super(Random, self).__init__("random")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Sample_stddev(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the sample standard deviation of inputs in the stream. This is less biased than stddev when you have a smaller population size.sample_stddev(by=None)sample_stddev(over=None)Returns reference to the input  object."""
        super(Sample_stddev, self).__init__("sample_stddev")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Sample_variance(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the sample variance of inputs in the stream. This is less biased than variance when you have a small sample sizesample_variance(by=None)sample_variance(over=None)Returns reference to the input  object."""
        super(Sample_variance, self).__init__("sample_variance")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Size(StreamMethod):
    def __init__(self, by=None, over=None):
        """Counts the number of inputs in the stream.size(by=None)size(over=None)Returns reference to the input  object."""
        super(Size, self).__init__("size")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Stddev(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the standard deviation of inputs in the stream.stddev(by=None)stddev(over=None)Returns reference to the input  object."""
        super(Stddev, self).__init__("stddev")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Sum(StreamMethod):
    def __init__(self, by=None, over=None):
        """Find the sum on a stream.sum(by=None)sum(over=None)Returns reference to the input  object."""
        super(Sum, self).__init__("sum")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Top(StreamMethod):
    def __init__(self, by=None, over=None):
        """Get the top values in the stream.top(count=None, percentage=None, by=None)Returns reference to the input  object."""
        super(Top, self).__init__("top")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Variance(StreamMethod):
    def __init__(self, by=None, over=None):
        """Calculates the variance of inputs in the stream.variance(by=None)variance(over=None)Returns reference to the input  object."""
        super(Variance, self).__init__("variance")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Integrate(StreamMethod):
    def __init__(self, by=None, over=None):
        """Multiplies the values of each input time series by the resolution (in seconds) of the computation. Integrate is most useful in SignalFx for gauge metrics.integrate()Returns reference to the input  object."""
        super(Integrate, self).__init__("integrate")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Map(StreamMethod):
    def __init__(self, by=None, over=None):
        """Apply a lambda function to a stream.map(mapfn)Returns reference to the input  object."""
        super(Map, self).__init__("map")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Publish(StreamMethod):
    def __init__(self, by=None, over=None):
        """Publish the output of a stream so that it is visible outside of a computation.publish(label=None)Returns reference to the input  object."""
        super(Publish, self).__init__("publish")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Timeshift(StreamMethod):
    def __init__(self, by=None, over=None):
        """Timeshift the datapoints for a stream, offset by a specified time period e.g. 1 week (1w), to enable comparison of time series with its own past behavior.timeshift(offset)Returns reference to the input stream object."""
        super(Timeshift, self).__init__("timeshift")
        self.args = [KWArg("by", by), KWArg("over", over)]
class Ewma(StreamMethod):
    def __init__(self, alpha):
        """Calculates the exponentially weighted moving average of the stream.
ewma(alpha)Returns a new  object."""
        super(Ewma, self).__init__("ewma")
        self.args = [StrArg(alpha)]
class Abs(StreamMethod):
    def __init__(self):
        """Apply absolute value to data in the stream.abs()Returns reference to the input  object."""
        super(Abs, self).__init__("abs")
        self.args = []
class Ceil(StreamMethod):
    def __init__(self):
        """Apply the ceil() function to data in the stream.ceil()Returns reference to the input  object."""
        super(Ceil, self).__init__("ceil")
        self.args = []
class Floor(StreamMethod):
    def __init__(self):
        """Apply floor() to data in the stream.floor()Returns reference to the input  object."""
        super(Floor, self).__init__("floor")
        self.args = []
class Log(StreamMethod):
    def __init__(self):
        """Apply the natural log function to data in the stream.log()Returns reference to the input  object."""
        super(Log, self).__init__("log")
        self.args = []
class Log10(StreamMethod):
    def __init__(self):
        """Apply the logarithm(base 10) function to data in the stream.log10()Returns reference to the input  object."""
        super(Log10, self).__init__("log10")
        self.args = []
class Pow(StreamMethod):
    def __init__(self, exponent):
        """ - return (stream data)"""
        super(Pow, self).__init__("pow")
        self.args = [StrArg(exponent)]
class Pow(StreamMethod):
    def __init__(self, base=None):
        """ - return base"""
        super(Pow, self).__init__("pow")
        self.args = [KWArg("base", base)]
class Scale(StreamMethod):
    def __init__(self, multiplier):
        """Scale data in the stream by a multiplierscale(multiplier)Returns reference to the input  object."""
        super(Scale, self).__init__("scale")
        self.args = [StrArg(multiplier)]
class Sqrt(StreamMethod):
    def __init__(self):
        """Apply a square root to data in the stream.sqrt()Returns reference to the input  object."""
        super(Sqrt, self).__init__("sqrt")
        self.args = []
class Above(StreamMethod):
    def __init__(self, limit, inclusive=None, clamp=None):
        """Only pass through data in the stream that is above a particular value, or clamp data above a value to that value.
above(limit, inclusive=False, clamp=False)Returns reference to the input  object."""
        super(Above, self).__init__("above")
        self.args = [StrArg(limit), KWArg("inclusive", inclusive), KWArg("clamp", clamp)]
class Below(StreamMethod):
    def __init__(self, limit, inclusive=None, clamp=None):
        """Only pass through data in the stream that is below a particular value, or clamp data below a value to that value.
below(limit, inclusive=False, clamp=False)Returns reference to the input  object."""
        super(Below, self).__init__("below")
        self.args = [StrArg(limit), KWArg("inclusive", inclusive), KWArg("clamp", clamp)]
class Between(StreamMethod):
    def __init__(self, low_limit, high_limit, low_inclusive=None, high_inclusive=None, clamp=None):
        """Only pass through data in the stream that is between two particular values or replace data that is not between two particular values with the limit that they are closest to.
between(low_limit, high_limit, low_inclusive=False, high_inclusive=False, clamp=False)Returns reference to the input  object."""
        super(Between, self).__init__("between")
        self.args = [StrArg(low_limit), StrArg(high_limit), KWArg("low_inclusive", low_inclusive), KWArg("high_inclusive", high_inclusive), KWArg("clamp", clamp)]
class Equals(StreamMethod):
    def __init__(self, value, replacement=None):
        """Only pass through data in the stream that is equal to a particular value or replace data that is not equal to a particular value with another value
equals(value, replacement=None)Returns reference to the input  object."""
        super(Equals, self).__init__("equals")
        self.args = [StrArg(value), KWArg("replacement", replacement)]
class Not_between(StreamMethod):
    def __init__(self, low_limit, high_limit, low_inclusive=None, high_inclusive=None):
        """Only pass through data in the stream that is not between two particular values
not_between(low_limit, high_limit, low_inclusive=False, high_inclusive=False)Returns reference to the input  object."""
        super(Not_between, self).__init__("not_between")
        self.args = [StrArg(low_limit), StrArg(high_limit), KWArg("low_inclusive", low_inclusive), KWArg("high_inclusive", high_inclusive)]
class Not_equals(StreamMethod):
    def __init__(self, value, replacement=None):
        """Only pass through data in the stream that is not equal to a particular value or replace data that is equal to a particular value with another value
not_equals(value, replacement=None)Returns reference to the input  object."""
        super(Not_equals, self).__init__("not_equals")
        self.args = [StrArg(value), KWArg("replacement", replacement)]
class Promote(StreamMethod):
    def __init__(self, property):
        """Promotes a metadata property to a dimension.promote(property), promote([property, ...]), promote(by=None), promote(property, ...)"""
        super(Promote, self).__init__("promote")
        self.args = [StrArg(property)]
