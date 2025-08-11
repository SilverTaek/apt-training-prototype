<template>
    <div class="send-mail" style="max-width:720px;margin:24px auto;padding:16px;border:1px solid #eee;border-radius:8px;">
      <h2>메일 발송 테스트</h2>
  
      <label>발송자 대표 이름</label>
      <input v-model="form.sender_name" type="text" placeholder="예: 보안교육 운영팀" />
  
      <label style="margin-top:8px;">발송자 이메일</label>
      <input v-model="form.sender" type="email" placeholder="예: training@company.com" />
  
      <label style="margin-top:8px;">메일 제목</label>
      <input v-model="form.subject" type="text" placeholder="예: [훈련] 사회공학 보안 교육" />
  
      <label style="margin-top:8px;">수신자 (쉼표 또는 줄바꿈으로 구분)</label>
      <textarea v-model="recipientsRaw" rows="3" placeholder="user1@ex.com, user2@ex.com&#10;user3@ex.com"></textarea>
  
      <label style="margin-top:8px;">메일 본문 (HTML)</label>
      <textarea v-model="form.html" rows="10" placeholder="<h1>안내</h1><p>본문 내용...</p>"></textarea>
  
      <div style="margin-top:12px;">
        <button @click="submit" :disabled="loading">발송</button>
        <span v-if="loading" style="margin-left:8px;">발송 중…</span>
      </div>
  
      <pre v-if="error" style="color:#b00020;white-space:pre-wrap;margin-top:12px;">{{ error }}</pre>
      <pre v-if="result" style="white-space:pre-wrap;margin-top:12px;">{{ result }}</pre>
    </div>
  </template>
  
  <script>
  export default {
    name: "SendMail",
    data() {
      return {
        form: {
          sender_name: "",
          sender: "",
          subject: "",
          html: "<h1>보안 훈련 안내</h1><p>이메일 본문 테스트입니다.</p>",
        },
        recipientsRaw: "",
        loading: false,
        error: "",
        result: "",
      };
    },
    methods: {
      parseRecipients(raw) {
        return raw
          .split(/[\n,;]/)        // 줄바꿈/쉼표/세미콜론 구분
          .map(s => s.trim())
          .filter(Boolean);
      },
      validate() {
        const to = this.parseRecipients(this.recipientsRaw);
        if (!to.length) return "수신자를 1명 이상 입력하세요.";
        if (!this.form.subject.trim()) return "메일 제목을 입력하세요.";
        if (!this.form.html.trim()) return "메일 본문(HTML)을 입력하세요.";
        // sender는 비워두면 서버에서 MAIL_FROM 사용 (선택 입력)
        return null;
      },
      async submit() {
        this.error = "";
        this.result = "";
        const err = this.validate();
        if (err) { this.error = err; return; }
  
        this.loading = true;
        try {
          const payload = {
            to: this.parseRecipients(this.recipientsRaw),
            subject: this.form.subject,
            html: this.form.html,
            sender: this.form.sender || null,
            sender_name: this.form.sender_name || null,
          };
          const res = await fetch("/mail/send", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          const json = await res.json();
          this.result = JSON.stringify(json, null, 2);
        } catch (e) {
          this.error = String(e);
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .send-mail input, .send-mail textarea {
    width: 100%;
    box-sizing: border-box;
    padding: 8px;
    margin-top: 4px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 14px;
  }
  .send-mail button {
    padding: 8px 14px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  </style>
  