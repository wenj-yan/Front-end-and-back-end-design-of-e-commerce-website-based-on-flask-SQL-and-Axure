document.addEventListener('DOMContentLoaded', function() {
    var text = document.getElementById('dynamic-text');
    var textLength = text.textContent.length * 2 + 'ms'; // 计算打字机效果的持续时间

    // 延迟打字机效果的开始
    setTimeout(function() {
        text.style.animationDuration = textLength;
        text.style.animationFillMode = 'forwards';
    }, 500);
});